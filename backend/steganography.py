from PIL import Image, PngImagePlugin
import os

def encode_image(image_path, secret_msg):
    img = Image.open(image_path)

    meta = PngImagePlugin.PngInfo()
    meta.add_text("secret_message", secret_msg)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(base_dir, "encoded.png")

    img.save(out_path, pnginfo=meta)
    return out_path


def decode_image(image_path):
    img = Image.open(image_path)
    return img.info.get("secret_message", "❌ No secret message found")
