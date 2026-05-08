from flask import Flask, request, jsonify, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flasgger import Swagger, swag_from

app = Flask(__name__)
app.secret_key = 'supersecretkey'
swagger = Swagger(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, role):
        self.id = id
        self.role = role

# Example users
users = {
    1: User(1, "admin"),
    2: User(2, "user"),
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

# 🔥 ONLY CHANGE DONE HERE (login now returns JSON)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        user = users.get(int(user_id))
        if user:
            login_user(user)

            return jsonify({
                "message": "Login successful",
                "id": user.id,
                "role": user.role
            })

    return '''
    <form method="POST">
        User ID: <input type="text" name="user_id"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/api/admin/v1/users/all', methods=['GET'])
@login_required
@swag_from({
    'responses': {
        200: {
            'description': 'A list of all users.',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'role': {'type': 'string'}
                    }
                }
            }
        }
    },
    'security': [
        {
            'basicAuth': []
        }
    ],
    'tags': ['Admin']
})
def get_users():
    users_list = [{"id": user.id, "role": user.role} for user in users.values()]
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9877)