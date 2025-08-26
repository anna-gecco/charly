# backend/app.py
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chatbot import chatbot_response

app = Flask(__name__, static_folder="../frontend", static_url_path="/")
CORS(app)  # erlaubt Zugriff vom Frontend (falls du Frontend separat hostest)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    msg = data.get("message", "").strip()
    if not msg:
        return jsonify({"answer": "Bitte gib eine Frage ein."}), 400
    answer = chatbot_response(msg)
    return jsonify({"answer": answer})

# optional: wenn du den Browser direkt auf http://localhost:5000 öffnest,
# liefert Flask die frontend/index.html zurück:
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # debug=True zeigt Fehler direkt im Terminal; für Entwicklung sinnvoll
    app.run(host="0.0.0.0", port=port, debug=True)