import requests
from flask import Flask, jsonify

app = Flask(__name__)

EXTERNAL_API = "http://127.0.0.1:5001/random"

@app.route('/api/quote')
def get_quote():

    response = requests.get(EXTERNAL_API)
    data = response.json()

    # ❌ NO VALIDATION (API10 issue)
    quote = data.get("content")

    return jsonify({
        "quote": quote,
        "source": data.get("source")
    })

app.run(port=9882)