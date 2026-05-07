from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/v1/images', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'Image uploaded and thumbnails created.'
        }
    },
    'parameters': [
        {
            'name': 'image_data',
            'in': 'formData',
            'type': 'string',
            'format': 'base64',
            'required': 'true',
            'description': 'Base64 encoded image data'
        }
    ],
    'consumes': [
        'multipart/form-data'
    ],
    'tags': ['Images']
})
def upload_image():
    image_data = request.form.get('image_data')
    if not image_data:
        return jsonify({"error": "Missing image data"}), 400

    # Process the image and create thumbnails
    # ...

    return jsonify({"message": "Image uploaded and thumbnails created."}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)