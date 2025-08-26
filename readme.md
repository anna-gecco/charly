# 🤖 FS-KI-Chatbot

Ein Chatbot mit:
- FAQ-Abfrage
- Fallback zu OpenAI GPT (günstiges Modell: gpt-4o-mini)
- Pinke Chat-Bubble für Webseiten (Frontend in HTML)

## 🚀 Deployment (Backend)
1. Repository auf GitHub hochladen.
2. Bei [Render](https://render.com) → "New Web Service".
3. Repository auswählen.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python app.py`
6. Environment Variable setzen:
   - `OPENAI_API_KEY` = Dein API Key

## 🌐 Frontend
- Öffne `frontend/index.html`
- Passe die Backend-URL (`fetch`) an deine Render-URL an.
- Kopiere den Inhalt nach WordPress (HTML-Block).

Fertig 🎉