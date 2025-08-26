from flask import Flask, request, jsonify
import pandas as pd
import os
from openai import OpenAI

# Flask App starten
app = Flask(__name__)

# OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# FAQ laden
faq_df = pd.read_csv("faq.csv")  # Stelle sicher, dass faq.csv im gleichen Ordner liegt

def search_faq(user_input):
    """
    Schnelle FAQ-Abfrage
    """
    for _, row in faq_df.iterrows():
        if row['frage'].lower() in user_input.lower():
            return row['antwort']
    return None

def get_ai_answer(user_input):
    """
    KI-Antwort, nur aufgerufen, wenn FAQ nichts liefert
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}],
            timeout=15  # maximal 15 Sekunden warten
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Fehler bei der KI-Antwort: {str(e)}"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    answer = search_faq(user_input)
    if not answer:
        answer = get_ai_answer(user_input)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
