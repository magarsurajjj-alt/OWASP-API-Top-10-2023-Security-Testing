from flask import Flask, request, jsonify
from flasgger import Swagger
import requests
import os

app = Flask(__name__)

# Swagger Config
app.config['SWAGGER'] = {
    'title': 'SSRF Vulnerable API Lab',
    'uiversion': 2
}

swagger = Swagger(app)

# Create images folder
os.makedirs("downloads", exist_ok=True)

# -----------------------------
# Public Route
# -----------------------------
@app.route('/')
def home():
    return jsonify({
        "message": "SSRF Lab Running"
    })


# -----------------------------
# Internal Admin Route
# -----------------------------
@app.route('/admin')
def admin():
    return jsonify({
        "admin_panel": True,
        "secret_key": "SUPER-SECRET-KEY",
        "internal_message": "This endpoint should not be public"
    })


# -----------------------------
# Fake Internal API
# -----------------------------
@app.route('/internal-api')
def internal_api():
    return jsonify({
        "database_password": "root123",
        "api_token": "INTERNAL-TOKEN-123"
    })


# -----------------------------
# SSRF Vulnerable Endpoint
# -----------------------------
@app.route('/api/fetch', methods=['POST'])
def fetch_url():

    data = request.json

    if not data or 'url' not in data:
        return jsonify({
            "error": "Missing URL"
        }), 400

    url = data['url']

    try:
        # Vulnerable request
        response = requests.get(url, timeout=5)

        # Save response content
        filename = url.replace("http://", "").replace("/", "_")
        filepath = os.path.join("downloads", f"{filename}.txt")

        with open(filepath, "wb") as f:
            f.write(response.content)

        return jsonify({
            "message": "URL fetched successfully",
            "requested_url": url,
            "status_code": response.status_code,
            "saved_file": filepath,
            "preview": response.text[:300]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# -----------------------------
# Run Application
# -----------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9878, debug=True)