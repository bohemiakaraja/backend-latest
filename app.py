from flask import Flask, request, send_file
from TTS.api import TTS
import os

app = Flask(__name__)

# Load the TTS model once
tts = TTS("tts_models/en/ljspeech/glow-tts").to("cpu")

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}, 400

    output_path = "output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return send_file(output_path, mimetype="audio/wav")

# Bind to Render's expected host and port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
