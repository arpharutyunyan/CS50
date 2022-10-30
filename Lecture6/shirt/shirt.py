"""
    After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt. No need to buy one online, 
    but like to try one on virtually?

    In a file called shirt.py, implement a program that expects exactly two command-line arguments:

    in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
    The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, 
    saving the result as its output.

    Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, 
    per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay 
    the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, 
    per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

    The program should instead exit via sys.exit:

    if the user does not specify exactly two command-line arguments,
    if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if the input’s name does not have the same extension as the output’s name, or
    if the specified input does not exist.
    Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt 
    appears to fit perfectly.

    If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py. 
    No need to submit any photos with your code. But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your 
    virtual shirt in any of CS50’s communities!
"""

import sys
import os.path
from PIL import Image, ImageOps


format = ("jpg", "jpeg", "png")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].split(".")[1].lower() not in format and sys.argv[2].split(".")[1].lower() not in format:
    sys.exit("Invalid output")
elif sys.argv[1].split(".")[1].lower() != sys.argv[2].split(".")[1].lower():
    sys.exit("Input and output have different extensions")
elif not (os.path.exists(sys.argv[1])):
    sys.exit("Input does not exist")


shirt = Image.open("shirt.png")
before = Image.open(sys.argv[1])
size = shirt.size
muppet = ImageOps.fit(before, size)

muppet.paste(shirt, shirt)
muppet.save(sys.argv[2])
