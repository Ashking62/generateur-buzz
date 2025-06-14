from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI  # nouvelle méthode

load_dotenv()

# Initialisation du client OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

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

    if not topic or not content_type:
        return jsonify({"error": "Champs 'topic' et 'type' requis"}), 400

    if content_type not in TYPES:
        return jsonify({"error": "Type invalide"}), 400

    prompt = f"{TYPES[content_type]} {topic}."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un expert en marketing viral."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.8
        )

        content = response.choices[0].message.content.strip()
        if not content:
            return jsonify({"error": "Aucune réponse générée"}), 500
        return jsonify({"content": content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


