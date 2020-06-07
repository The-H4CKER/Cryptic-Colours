nigel.a.jacob@gmail.com

# Cryptic Colours
Content Creators Club CTF Challenge
 
## Flag
Flag: R3d_6r3En_81u3

## Briefing
Download the image file at https://github.com/The-H4CKER/Cryptic-Colours/blob/master/build/web/img.zip?raw=true (probably a different link). Decode the message encrypted in the image to reveal the flag.

By [username].

## Infrastructure
- Host the download file.

## Risks
The challenge involves identifying text hidden in an image, so there are no significant risks, as far as I can see.

## Walkthrough
The student will identify the RGB values of each of the main colours in the image, either on the VM by using GIMP's colour picker tool or online with a site such as https://imagecolorpicker.com/en/.

Doing this for each of the 7 images in order will generate a list of 21 decimal (or hexadecimal) numbers between 0 (00) and 255 (FF) (inclusive). These, when converted to ASCII, will return the flag.

This whole process can also be automated using a simple Python script (with the Pillow module) to generate the flag. The script code can be found in the src folder.
