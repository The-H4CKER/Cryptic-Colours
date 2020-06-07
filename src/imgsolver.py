#!/usr/bin/python3
from PIL import Image

image = Image.open("img.PNG") #opens image
pixels = []

for i in range(len(image.getcolors())):
    x = i*image.size[0]/len(image.getcolors())
    pixels.append(list(image.getpixel((x,0))[:-1]))

msg = "".join(["".join([chr(p) for p in pixel]) for pixel in pixels])

print(msg)

