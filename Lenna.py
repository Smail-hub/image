from PIL import Image

image = Image.open("lenna.jpg")
print(image.mode)
RGB_image = image.convert("RGB")
RGB_image.save("RGB_image.jpg")
print(RGB_image.mode)
