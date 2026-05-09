from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/random')
def fake_data():
    return jsonify({
        "content": "<script>alert('API10 ATTACK')</script>",
        "source": "evil-api"
    })

app.run(port=5001)