"""
ApexCharmCropper.py

Crops weapon charm images from Apex Legends for use on the Apex Legends Wiki.

Author - Sam Carroll
2/14/2023
"""
import os
from PIL import Image

image_count = 0

# Take user input for folder path and sets as the working directory.
directory = os.fsencode(input("Type the path of the image folder to be cropped: "))
directory_name = str(directory)[2:len(str(directory)) - 1]

# Iterates through each file in the folder.
for file in os.listdir(directory):
    relative_filename = str(os.fsdecode(file))
    filename = directory_name + "\\" + relative_filename

    # Skips non-PNG files
    if not filename.endswith(".png"):
        continue

    img = Image.open(filename)

    # Charms
    if relative_filename.startswith("Charms "):
        img2 = img.crop((700, 300, 700 + 800, 300 + 600))
        img2.save(filename)

    # All other images
    else:
        continue

    image_count = image_count + 1
    print(str(image_count) + " | Cropped " + filename)

print("Cropped " + str(image_count) + " images.")
    