from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Configure OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ajoute ta clé dans les variables d'environnement

# Types de contenu disponibles
TYPES = {
    "facebook": "Écris un post Facebook engageant sur",
    "twitter": "Écris un tweet viral de moins de 280 caractères sur",
    "instagram": "Écris une légende Instagram captivante sur",
    "tiktok": "Écris un script court pour une vidéo TikTok sur"
}

@app.route("/")
def index():
    return render_template("index.html", types=TYPES.keys())

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    topic = data.get("topic")
    content_type = data.get("type")

    if content_type not in TYPES:
        return jsonify({"error": "Type invalide"}), 400

    prompt = f"{TYPES[content_type]} {topic}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un expert en marketing viral."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.8
        )
        content = response["choices"][0]["message"]["content"].strip()
        return jsonify({"content": content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
