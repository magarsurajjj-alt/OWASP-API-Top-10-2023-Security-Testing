from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger, swag_from

app = Flask(__name__)
auth = HTTPBasicAuth()
Swagger(app)

users = {
    "user1": "password1",
    "user2": "password2"
}

@auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/', methods=['GET'])
def home():
    return "user1:password1"

@app.route('/api/video/update_video', methods=['PUT'])
@swag_from({
    'responses': {
        200: {
            'description': 'Video updated',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'blocked': {'type': 'boolean'}
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'type': 'object',
                'properties': {
                    'description': {'type': 'string'}
                }
            }
        }
    ]
})
def update_video():
    data = request.get_json()

    video = {
        "id": 1,
        "title": "Example Video",
        "description": "A sample video",
        "blocked": True
    }

    # ❌ VULNERABLE: no property restriction
    for key in data:
        video[key] = data[key]

    return jsonify(video)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9875)