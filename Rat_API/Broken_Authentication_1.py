from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
Swagger(app)

users = {
    "user1": generate_password_hash("password1"),
    "user2": generate_password_hash("password2")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return username

@app.route('/api/signup', methods=['POST'])
def signup():
    """
    Create a new user
    ---
    parameters:
      - name: username
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    responses:
      200:
        description: User created successfully
    """
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = generate_password_hash(password)
    return jsonify({"message": "User created successfully"}), 200

@app.route('/api/secure', methods=['GET'])
@auth.login_required
def secure_endpoint():
    """
    A secure endpoint that requires authentication
    ---
    responses:
      200:
        description: Successfully accessed the secure endpoint
    """
    return jsonify({"message": "You have accessed the secure endpoint!"}), 200

@app.route('/api/secure/<username>', methods=['GET'])
@auth.login_required
def secure_endpoint_with_param(username):
    """
    A secure endpoint that requires authentication and accepts a parameter
    ---
    parameters:
      - name: username
        in: path
        type: string
        required: true
    responses:
      200:
        description: Successfully accessed the secure endpoint
    """
    return jsonify({"message": "You have accessed the secure endpoint!"}), 200

# make an endpoint to change the usertype to admin
@app.route("/api/users/<int:user_id>/usertype", methods=["PUT"])
@auth.login_required
def change_usertype(user_id):
    user = find_user_by_id(user_id)
    if user:
        # BOLA vulnerability - No authorization check for updating the document
        users[0]["usertype"] = "admin"
        return jsonify({"message": "User type updated successfully"})
    return jsonify({"error": "User not found"}), 404

# make find_user_by_id
def find_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9874)