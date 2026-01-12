import os
from PIL import Image, ImageFilter

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "500px-Lenna.png")

image = Image.open(file_path)
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))
blurred_image.save(os.path.join(script_dir, "Lenna_blurred_result.png"))
