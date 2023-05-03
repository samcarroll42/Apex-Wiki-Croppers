"""
DeleteJFIF.py

Quickly deletes JFIF or JPEG files from a folder.

Author - Sam Carroll
Written - 2/14/2023
Last updated - 5/3/2023
"""
import os
from PIL import Image

image_count = 0

# Take user input for folder path and sets as the working directory.
directory = os.fsencode(input("Type the path of the image folder to be cropped: "))
directory_name = str(directory)[2:len(str(directory)) - 1]

# Iterates through each file in the folder.
for file in os.listdir(directory):
    filename = directory_name + "\\" + str(os.fsdecode(file))

    if filename.endswith(".jfif") or filename.endswith(".jpg"):
        os.remove(filename)
    else:
        continue

    image_count = image_count + 1
    print(str(image_count) + " | Deleted " + filename)

print("Deleted " + str(image_count) + " images.")