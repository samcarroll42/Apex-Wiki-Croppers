"""
ApexMobileSkinCropper.py

Crops legend skins from Apex Legends Mobile for use on the Apex Legends Wiki.

NOTICE: As Apex Legends Mobile was shut down on 5/1/2023, this script has been deprecated.

Author - Sam Carroll
2/14/2023
"""
import os
from PIL import Image

image_count = 0
legend_tuple = ("Ash Mobile.png", "Bangalore Mobile.png", "Revenant Mobile.png", "Pathfinder Mobile.png", "Wraith Mobile.png", "Mirage Mobile.png", 
"Octane Mobile.png", "Horizon Mobile.png", "Valkyrie Mobile.png", "Bloodhound Mobile.png", "Crypto Mobile.png", "Gibraltar Mobile.png",
"Lifeline Mobile.png", "Loba Mobile.png", "Caustic Mobile.png", "Fade Mobile.png", "Rhapsody Mobile.png")

# Take user input for folder path and sets as the working directory.
directory = os.fsencode(input("Type the path of the image folder to be cropped: "))
directory_name = str(directory)[2:len(str(directory)) - 1]

# Iterates through each file in the folder.
for file in os.listdir(directory):
    filename = directory_name + "\\" + str(os.fsdecode(file))

    # Skips non-PNG files
    if not filename.endswith(".png"):
        continue

    img = Image.open(filename)

    # legends
    if filename.endswith(legend_tuple):
        img2 = img.crop((620, 22, 620 + 550, 22 + 750))
        img2.save(filename)

    # All other images
    else:
        continue

    image_count = image_count + 1
    print(str(image_count) + " | Cropped " + filename)

print("Cropped " + str(image_count) + " images.")