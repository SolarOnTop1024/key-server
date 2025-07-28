from flask import Flask, request, jsonify
import json
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Key server is up."

@app.route("/validate")
def validate_key():
    key = request.args.get("key")
    uid = request.args.get("id")

    if not key or not uid:
        return jsonify({"valid": False, "error": "Missing key or id"})

    # Load keys
    if not os.path.exists("keys.json"):
        return jsonify({"valid": False, "error": "keys.json missing"})

    with open("keys.json", "r") as f:
        keys = json.load(f)

    # Key validation logic
    if uid in keys:
        entry = keys[uid]
        if entry["key"] == key and entry["active"]:
            try:
                expires = datetime.datetime.strptime(entry["expires"], "%Y-%m-%d").date()
                if datetime.date.today() <= expires:
                    return jsonify({"valid": True})
            except:
                return jsonify({"valid": False, "error": "Invalid date format"})

    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
