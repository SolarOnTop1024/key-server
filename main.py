from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/validate")
def validate():
    key = request.args.get("key")
    user_id = request.args.get("id")

    with open("keys.json", "r") as f:
        data = json.load(f)

    if user_id in data:
        entry = data[user_id]
        if entry["key"] == key and entry["active"]:
            return jsonify({"valid": True, "expires": entry["expires"]})

    return jsonify({"valid": False})

# Make sure this matches your Render port config
import os
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
