"""
JFIFtoPNG.py

Converts JFIF files to PNG format.

Author - Sam Carroll
2/14/2023
"""
import os
from PIL import Image

image_count = 0
filetype_tuple = (".jpg", ".jpeg", ".jfif")

# Take user input for folder path and sets as the working directory.
directory = os.fsencode(input("Type the path of the image folder to be processed: "))
directory_name = str(directory)[2:len(str(directory)) - 1]

# Iterates through each file in the folder.
for file in os.listdir(directory):
    filename = directory_name + "\\" + str(os.fsdecode(file))
    relative_filename = filename[0:filename.find(".")]

    # Skips non-PNG files
    if not filename.endswith(filetype_tuple):
        continue

    img = Image.open(filename)
    img.save(relative_filename + ".png")

    image_count = image_count + 1
    print(str(image_count) + " | Converted " + filename)

print("Converted " + str(image_count) + " images.")