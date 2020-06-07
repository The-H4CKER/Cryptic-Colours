nigel.a.jacob@gmail.com

# Cryptic Colours
Content Creators Club CTF Challenge
 
## Flag
Flag: R3d_6r3En_81u3

## Briefing
Download the files at [url].

By [username].

## Infrastructure
- Host the download file.

## Risks
The challenge involves identifying text hidden in an image, so there are no significant risks.

## Walkthrough
The student will identify the RGB values of each of the main colours in the image, either on the VM by using GIMP's colour picker tool or online with a site such as https://imagecolorpicker.com/en/.

Doing this for each of the 7 images in order will generate a list of 21 decimal (or hexadecimal) numbers between 0 (00) and 255 (FF) (inclusive). These, when converted to ASCII, will return the flag.

This whole process can also be automated using a simple Python script as shown below:

#!/usr/bin/python3

from PIL import Image

image = Image.open("img.PNG") #opens image
pixels = []

for i in range(len(image.getcolors())):
    x = i*image.size[0]/len(image.getcolors())
    pixels.append(list(image.getpixel((x,0))[:-1]))

msg = "".join(["".join([chr(p) for p in pixel]) for pixel in pixels])

print(msg)

