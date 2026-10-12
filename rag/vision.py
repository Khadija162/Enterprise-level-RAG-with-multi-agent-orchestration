"""VLM-ready image metadata interface; never invent image descriptions."""
from io import BytesIO
from PIL import Image, ImageStat


def analyze_image(raw: bytes) -> dict:
    if len(raw) > 4_000_000:
        raise ValueError("Max image size 4MB")
    try:
        image = Image.open(BytesIO(raw))
        image.verify()
        image = Image.open(BytesIO(raw)).convert("RGB")
    except Exception as exc:
        raise ValueError("Invalid image") from exc
    if image.width * image.height > 12_000_000:
        raise ValueError("Image dimensions exceed limit")
    return {"width": image.width, "height": image.height,
            "mean_luminance": round(ImageStat.Stat(image.convert("L")).mean[0], 2),
            "mode": "metadata_only",
            "note": "VLM model integration is planned; no semantic image interpretation is performed."}
