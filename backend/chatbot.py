def get_bot_reply(user_msg):
    msg = user_msg.lower().strip()

    # ---------- WHAT IS ENCODE ----------
    if "what is encode" in msg or "what is encoding" in msg:
        return {
            "answer": (
                "🔐 *What is Encoding?*\n\n"
                "Encoding is the process of hiding a secret message inside an image.\n"
                "In Silent Pixels, the message is embedded in the image so that\n"
                "no one can see it normally."
            )
        }

    # ---------- HOW TO USE ENCODE ----------
    if "how to encode" in msg or "how to use encode" in msg:
        return {
            "answer": (
                "🛠 *How to use Encode (Steps):*\n\n"
                "1️⃣ Go to the Encode page\n"
                "2️⃣ Select a PNG image\n"
                "3️⃣ Enter your secret message\n"
                "4️⃣ Click Encode\n"
                "5️⃣ Download the encoded image\n\n"
                "📥 You can later decode this image to read the message."
            )
        }

    # ---------- PURPOSE OF ENCODE ----------
    if "purpose of encode" in msg or "why encode" in msg:
        return {
            "answer": (
                "🎯 *Purpose of Encoding:*\n\n"
                "• To send secret messages securely\n"
                "• To prevent unauthorized access\n"
                "• To hide information inside images\n"
                "• Used in secure communication and data privacy"
            )
        }

    # ---------- QUICK ENCODE ----------
    if "encode" in msg:
        return {
            "answer": (
                "🔐 *Encode Feature*\n\n"
                "Encoding hides your secret message inside an image.\n"
                "Would you like to know:\n"
                "• What is Encode?\n"
                "• How to use Encode?\n"
                "• Purpose of Encode?"
            ),
            "quick_replies": [
                "What is Encode?",
                "How to use Encode?",
                "Purpose of Encode"
            ]
        }

    # ---------- DECODE ----------
    if "decode" in msg:
        return {
            "answer": (
                "🔓 *Decode Feature*\n\n"
                "Decoding extracts the hidden message from an encoded image.\n\n"
                "Steps:\n"
                "1️⃣ Go to Decode page\n"
                "2️⃣ Upload encoded image\n"
                "3️⃣ Click Decode\n"
                "4️⃣ Secret message will be shown"
            )
        }

    # ---------- IMAGE GENERATION ----------
    if ("generate" in msg and "image" in msg):
        return {
            "answer": "🖼 Here is a sample secure image used in Silent Pixels.",
            "image": "/static/generated_image.png"
        }

    # ---------- PROJECT INFO ----------
    if "silent pixels" in msg or "project" in msg:
        return {
            "answer": (
                "📌 *Silent Pixels Project*\n\n"
                "Silent Pixels is a steganography-based security application\n"
                "that hides secret messages inside images.\n\n"
                "It includes Encode, Decode, and an intelligent chatbot."
            )
        }

    # ---------- FALLBACK ----------
    return {
        "answer": (
            "🤖 I can help you with:\n"
            "• Encode\n"
            "• Decode\n"
            "• What is Encode\n"
            "• How to use Encode\n"
            "• Purpose of Encode\n"
            "• Generate Image"
        ),
        "quick_replies": [
            "What is Encode?",
            "How to use Encode?",
            "Purpose of Encode",
            "Generate Image"
        ]
    }
