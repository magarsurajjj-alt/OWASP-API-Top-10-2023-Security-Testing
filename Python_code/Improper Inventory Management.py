from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
import time

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'OWASP API9 Demo',
    'uiversion': 3
}

swagger = Swagger(app)

# -----------------------------
# Fake Database
# -----------------------------
users = [
    {
        "id": 1,
        "email": "admin@test.com",
        "password": "admin123",
        "role": "admin",
        "token": "admin-token"
    },
    {
        "id": 2,
        "email": "user@test.com",
        "password": "user123",
        "role": "user",
        "token": "user-token"
    }
]

# =========================================================
# SECURE API VERSION (VISIBLE IN SWAGGER)
# =========================================================

@app.route('/api/v2/login', methods=['POST'])
@swag_from({
    'tags': ['Secure API v2'],
    'description': 'Secure login endpoint',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string'},
                    'password': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        '200': {'description': 'Login successful'},
        '401': {'description': 'Invalid credentials'}
    }
})
def login_v2():

    data = request.json

    if not data:
        return jsonify({"message": "Missing JSON"}), 400

    email = data.get('email')
    password = data.get('password')

    for user in users:
        if user['email'] == email and user['password'] == password:

            # Simulated secure token response
            return jsonify({
                "message": "Login successful (v2)",
                "token": user['token']
            })

    return jsonify({"message": "Invalid credentials"}), 401


# =========================================================
# OLD / FORGOTTEN API VERSION (NOT DOCUMENTED)
# =========================================================

@app.route('/api/v1/login', methods=['POST'])
def login_v1():

    data = request.json

    if not data:
        return jsonify({"message": "Missing JSON"}), 400

    email = data.get('email')
    password = data.get('password')

    # VULNERABILITY:
    # plaintext password logging
    print(f"[V1 LOG] Email: {email} Password: {password}")

    for user in users:
        if user['email'] == email and user['password'] == password:

            # VULNERABILITY:
            # exposes sensitive data
            return jsonify({
                "message": "Login successful (v1)",
                "user": user
            })

    return jsonify({"message": "Invalid credentials"}), 401


# =========================================================
# FORGOTTEN ADMIN PANEL
# =========================================================

@app.route('/api/v1/admin/users', methods=['GET'])
def admin_users_v1():

    # NO AUTHENTICATION

    return jsonify({
        "users": users
    })


# =========================================================
# DEBUG ENDPOINT
# =========================================================

@app.route('/debug/config', methods=['GET'])
def debug_config():

    return jsonify({
        "debug": True,
        "server": "development",
        "database": "mysql://root:root@localhost/testdb",
        "secret_key": "SUPER_SECRET_KEY"
    })


# =========================================================
# INTERNAL TEST ENDPOINT
# =========================================================

@app.route('/internal/test', methods=['GET'])
def internal_test():

    return jsonify({
        "message": "Internal API exposed publicly"
    })


# =========================================================
# SLOW LEGACY ENDPOINT
# =========================================================

@app.route('/api/v1/slow-data', methods=['GET'])
def slow_data():

    time.sleep(5)

    return jsonify({
        "message": "Old slow endpoint"
    })


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route('/')
def home():

    return jsonify({
        "message": "OWASP API9 Improper Inventory Management Demo"
    })


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9881, debug=True)