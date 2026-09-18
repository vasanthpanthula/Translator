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
# Google Web Translation
# ---------------------------------------

def translate_google_web(text, source, target):
    try:
        url = "https://translate.googleapis.com/translate_a/single"

        params = {
            "client": "gtx",
            "sl": source,
            "tl": target,
            "dt": "t",
            "q": text
        }

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=15
        )

        if response.status_code != 200:
            print("Google Web Status:", response.status_code)
            return None

        data = response.json()

        if not data or not data[0]:
            return None

        translated_parts = []

        for item in data[0]:
            if item and item[0]:
                translated_parts.append(item[0])

        result = "".join(translated_parts).strip()

        if result:
            print("Google Web Translation Success")
            return result

        return None

    except Exception as e:
        print("Google Web Translation Error:", e)
        return None


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

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=15
        )

        if response.status_code != 200:
            print("MyMemory Status:", response.status_code)
            return None

        data = response.json()

        result = data.get(
            "responseData",
            {}
        ).get(
            "translatedText"
        )

        if result:
            result = result.strip()

        # MyMemory can return an error-like result
        if not result:
            return None

        if result.lower() == text.lower():
            print("MyMemory returned original text")
            return None

        print("MyMemory Translation Success")

        return result

    except Exception as e:
        print("MyMemory Error:", e)
        return None


# ---------------------------------------
# Deep Translator / Google
# ---------------------------------------

def translate_google(text, source, target):
    try:
        result = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        if result:
            print("Deep Translator Success")
            return result.strip()

        return None

    except Exception as e:
        print("Deep Translator Error:", e)
        return None


# ---------------------------------------
# Translation Function
# ---------------------------------------

def perform_translation(text, source, target):

    # 1. Google Web Translation
    translated = translate_google_web(
        text,
        source,
        target
    )

    if translated:
        return translated

    # 2. MyMemory
    translated = translate_mymemory(
        text,
        source,
        target
    )

    if translated:
        return translated

    # 3. Deep Translator
    translated = translate_google(
        text,
        source,
        target
    )

    if translated:
        return translated

    return None


# ---------------------------------------
# Home Page
# ---------------------------------------

@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


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

    try:
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

        print(
            f"Translation request: "
            f"{source} -> {target} | {text}"
        )

        translated = perform_translation(
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
            "message": (
                "Translation service is temporarily "
                "unavailable. Please try again."
            )
        })

    except Exception as e:

        print("Translation Route Error:", e)

        return jsonify({
            "success": False,
            "message": "Unable to translate the text."
        })


# ---------------------------------------
# TEXT TO SPEECH
# ---------------------------------------

@app.route(
    "/speak",
    methods=["POST"]
)
def speak():

    try:

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
            "message": (
                "Text-to-speech is temporarily "
                "unavailable."
            )
        })


# ---------------------------------------
# START APPLICATION
# ---------------------------------------

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )