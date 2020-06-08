nigel.a.jacob@gmail.com

# Cryptic Colours
Content Creators Club CTF Challenge
 
## Flag
Flag: R3d_6r3En_81u3

## Briefing
Download the image file at https://github.com/The-H4CKER/Cryptic-Colours/blob/master/build/web/img.zip?raw=true (probably use a different link). Decode the message encrypted in the image to reveal the flag.

By [username].

## Infrastructure
- Host the download file.

## Risks
The challenge involves identifying text hidden in an image, so there are no significant risks, as far as I can see.

## Walkthrough
The student will identify the RGB values of each of the colours in the image (from left to right), either on the VM by using GIMP's colour picker tool or online with a site such as https://imagecolorpicker.com/en/.

Doing this for each of the seven colours, in order, will generate a list of twenty-one decimal (or hexadecimal) numbers between 0 (00) and 255 (FF) (inclusive). The numbers must then be converted from a to ASCII characters which will reveal a message containing the flag.

This whole process can also be automated using a simple Python script (with the Pillow module) to generate the flag. The Pythonscript can be located in the src folder.
