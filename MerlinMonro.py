from PIL import Image

image = Image.open("monro.jpg")
print(image.mode)
red, blue, green = image.split()
new_image = Image.merge("RGB", (red, blue, green))
new_image.save("new_image.jpg")