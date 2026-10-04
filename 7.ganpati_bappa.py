from pathlib import Path
from PIL import Image

folder = Path(__file__).resolve().parent
image_files = [
    folder / "ganpati_bappa_royal.png",
    folder / "ganpati_bappa_morning.png",
]

for image_path in image_files:
    if image_path.exists():
        image = Image.open(image_path)
        print(f"{image_path.name}: {image.size[0]} x {image.size[1]} pixels")
        image.show()
    else:
        print(f"Image Not Found: {image_path}")
  