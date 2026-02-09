from PIL import Image, ImageDraw, ImageFont
from typing import List


def dummy_generate(prompt: str, style: str) -> List[Image.Image]:
    """Return placeholder images for UI testing."""
    imgs = []
    for i in range(2):
        img = Image.new("RGB", (1280, 720), color=(30 + i * 20, 40 + i * 10, 60 + i * 5))
        d = ImageDraw.Draw(img)
        text = f"{style}\n{prompt}\n#{i+1}"
        try:
            font = ImageFont.load_default()
        except Exception:
            font = None
        d.multiline_text((30, 30), text, fill=(255, 255, 255), font=font)
        imgs.append(img)
    return imgs
