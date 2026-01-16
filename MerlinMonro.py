from PIL import Image

image = Image.open("monro.jpg")
print(image.mode) 
red, green, blue = image.split() 
red.save("red_channel.jpg")
green.save("green_channel.jpg") 
blue.save("blue_channel.jpg") 