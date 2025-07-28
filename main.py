from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Solar Key Server is running."

@app.route("/validate")
def validate_key():
    key = request.args.get("key")
    uid = request.args.get("id")

    try:
        with open("keys.json", "r") as f:
            keys = json.load(f)
    except Exception as e:
        return jsonify({"valid": False, "error": str(e)})

    if uid in keys:
        data = keys[uid]
        if data["key"] == key and data["active"]:
            expires = datetime.datetime.strptime(data["expires"], "%Y-%m-%d").date()
            if datetime.date.today() <= expires:
                return jsonify({"valid": True})

    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
