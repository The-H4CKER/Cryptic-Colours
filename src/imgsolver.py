#!/usr/bin/python3
from PIL import Image

image = Image.open("img.PNG") #opens image file
pixels = [] #list of image data

for i in range(len(image.getcolors())):
    x = i*image.size[0]/len(image.getcolors())
    #generates different x-position for each colour
    pixels.append(list(image.getpixel((x,0))[:-1]))
    #adds the RGB value of each colour to pixels list

msg = "".join(["".join([chr(p) for p in pixel]) for pixel in pixels])
#converts nested list to string
print(msg)
