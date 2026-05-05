from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_token(username):
    return 'dsfgfd'

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request body
    username = request.json.get('username')
    password = request.json.get('password')

    # Validate the username and password
    if not username or not password:
        return jsonify({'message': 'Please provide a username and password.'}), 400

    # Authenticate the user
    if username == 'admin' and password == 'password':
        # Generate and return an authentication token
        token = generate_token(username)
        return jsonify({'token': token}), 200

    # Return an error message if authentication fails
    return jsonify({'message': 'Invalid username or password.'}), 401