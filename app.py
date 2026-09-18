from flask import Flask, render_template, request, jsonify, send_file
from deep_translator import GoogleTranslator
from gtts import gTTS
import requests
import io
import os

app = Flask(__name__)

LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Marathi": "mr"
}


# ---------------------------------------
# MyMemory Translation
# ---------------------------------------

def translate_mymemory(text, source, target):

    try:

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": f"{source}|{target}"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()

        result = data.get(
            "responseData",
            {}
        ).get(
            "translatedText"
        )

        return result

    except Exception as e:

        print("MyMemory Error:", e)

        return None


# ---------------------------------------
# Google Translation
# ---------------------------------------

def translate_google(text, source, target):

    try:

        result = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        return result

    except Exception as e:

        print("Google Translation Error:", e)

        return None


# ---------------------------------------
# Home Page
# ---------------------------------------

@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/")
def home():

    return render_template(
        "index.html",
        languages=LANGUAGES
    )


# ---------------------------------------
# TRANSLATE
# ---------------------------------------

@app.route(
    "/translate",
    methods=["POST"]
)
def translate():

    data = request.get_json()

    if not data:

        return jsonify({
            "success": False,
            "message": "Invalid request."
        })


    text = data.get(
        "text",
        ""
    ).strip()

    source = data.get(
        "source",
        "en"
    )

    target = data.get(
        "target",
        "te"
    )


    if not text:

        return jsonify({
            "success": False,
            "message": "Please enter some text."
        })


    # Same language

    if source == target:

        return jsonify({
            "success": True,
            "translation": text
        })


    # Try MyMemory

    translated = translate_mymemory(
        text,
        source,
        target
    )


    if translated:

        return jsonify({
            "success": True,
            "translation": translated
        })


    # Try Google

    translated = translate_google(
        text,
        source,
        target
    )


    if translated:

        return jsonify({
            "success": True,
            "translation": translated
        })


    return jsonify({
        "success": False,
        "message":
            "Translation service is temporarily unavailable."
    })


# ---------------------------------------
# TEXT TO SPEECH
# ---------------------------------------

@app.route(
    "/speak",
    methods=["POST"]
)
def speak():

    data = request.get_json()

    if not data:

        return jsonify({
            "success": False,
            "message": "Invalid request."
        })


    text = data.get(
        "text",
        ""
    ).strip()

    language = data.get(
        "language",
        "te"
    )


    if not text:

        return jsonify({
            "success": False,
            "message": "Nothing to speak."
        })


    try:

        # Create speech in memory

        audio = io.BytesIO()

        tts = gTTS(
            text=text,
            lang=language,
            slow=False
        )

        tts.write_to_fp(audio)

        audio.seek(0)


        return send_file(
            audio,
            mimetype="audio/mpeg"
        )


    except Exception as e:

        print("TTS Error:", e)

        return jsonify({
            "success": False,
            "message":
                "Text-to-speech is temporarily unavailable."
        })


# ---------------------------------------
# START APPLICATION
# ---------------------------------------

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )