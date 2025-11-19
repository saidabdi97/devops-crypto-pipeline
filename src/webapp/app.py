from flask import Flask, jsonify
from crypto_api import get_crypto_prices

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "App running",
        "message": "Crypto API pipeline in progress"
    })

@app.route("/prices")
def prices():
    data = get_crypto_prices()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


