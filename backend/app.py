import os
from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS

from steganography import encode_image, decode_image
from chatbot import get_bot_reply   # ✅ ADD THIS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
ENCODED_FILE = os.path.join(BASE_DIR, "encoded.png")

app = Flask(
    __name__,
    static_folder=STATIC_DIR,
    static_url_path="/static"
)
CORS(app)


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")
# ---------------- ENCODE ----------------
@app.route("/encode", methods=["POST"])
def encode():
    image = request.files["image"]
    message = request.form["message"]

    input_path = os.path.join(BASE_DIR, "input.png")
    image.save(input_path)

    encode_image(input_path, message)

    return render_template("encode.html",sucess= "image encoded successfully")

# ---------------- DOWNLOAD ----------------
@app.route("/download", methods=["GET"])
def download():
    return send_file(
        ENCODED_FILE,
        as_attachment=True,
        download_name="encoded.png"
    )


# ---------------- DECODE ----------------
@app.route("/decode", methods=["POST"])
def decode():
    image = request.files["image"]

    decode_path = os.path.join(BASE_DIR, "decode.png")
    image.save(decode_path)

    message = decode_image(decode_path)

    return render_template("decode.html",secret_message=message)


# ---------------- CHATBOT ----------------
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")

    reply = get_bot_reply(user_message)
    return jsonify(reply)


# ---------------- RUN ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
