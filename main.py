from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route("/validate")
def validate():
    key = request.args.get("key")
    with open("keys.json", "r") as f:
        data = json.load(f)

    for user_id in data:
        entry = data[user_id]
        if entry["key"] == key and entry["active"]:
            return jsonify({"valid": True, "expires": entry["expires"]})

    return jsonify({"valid": False})

# ✅ Render-compatible port setup
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
