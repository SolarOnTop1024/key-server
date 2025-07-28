from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route("/validate")
def validate():
    key = request.args.get("key")
    user_id = request.args.get("id")

    with open("keys.json", "r") as f:
        data = json.load(f)

    # Check both key and user ID
    if user_id in data:
        record = data[user_id]
        if record["key"] == key and record["active"]:
            return jsonify({"valid": True, "expires": record["expires"]})

    return jsonify({"valid": False})

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
