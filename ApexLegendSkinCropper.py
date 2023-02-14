import os
from PIL import Image

legendW = 546
legendH = 858

#C:\Users\samca\OneDrive\Desktop\Test Folder

# Take user input for folder path and sets as the working directory.
directory = os.fsencode(input("Type the path of the image folder to be cropped: "))
directory_name = str(directory)[2:len(str(directory)) - 1]

# Iterates through each file in the folder.
for file in os.listdir(directory):
    filename = directory_name + "\\" + str(os.fsdecode(file))
    img = Image.open(filename)

    # Ash
    if filename.endswith("Ash.png"):
        continue

    # Bangalore
    if filename.endswith("Bangalore.png"):
        img2 = img.crop((931, 204, 931 + legendW, 204 + legendH))
        img2.save(filename)
        print("Cropped " + filename)

    # Bloodhound
    if filename.endswith("Bloodhound.png"):
        continue
    
    # Catalyst
    if filename.endswith("Catalyst.png"):
        continue

    # Caustic
    if filename.endswith("Caustic.png"):
        continue

    # Crypto
    if filename.endswith("Crypto.png"):
        continue

    # Fuse
    if filename.endswith("Fuse.png"):
        continue

    # Gibraltar
    if filename.endswith("Gibraltar.png"):
        continue

    # Horizon
    if filename.endswith("Horizon.png"):
        continue

    # Lifeline
    if filename.endswith("Lifeline.png"):
        continue

    # Loba
    if filename.endswith("Loba.png"):
        continue

    # Mad Maggie
    if filename.endswith("Maggie.png"):
        continue

    # Mirage
    if filename.endswith("Mirage.png"):
        continue

    # Newcastle
    if filename.endswith("Newcastle.png"):
        continue

    # Octane
    if filename.endswith("Octane.png"):
        continue

    # Pathfinder
    if filename.endswith("Pathfinder.png"):
        continue

    # Rampart
    if filename.endswith("Rampart.png"):
        continue

    # Revenant
    if filename.endswith("Revenant.png"):
        continue

    # Seer
    if filename.endswith("Seer.png"):
        continue

    # Valkyrie
    if filename.endswith("Valkyrie.png"):
        continue

    # Vantage
    if filename.endswith("Vantage.png"):
        continue

    # Wattson
    if filename.endswith("Wattson.png"):
        continue

    # Wraith
    if filename.endswith("Wraith.png"):
        continue

# Go to folder path

# Iterate over files
    # For file in folder:
        # Check which Legend skin belongs to (ex. endswith(Bangalore.png))

        # Use Pillow to crop image to specified coordinates

        # If file is for weapon / charm / not applicable:
            # Skip/continue

    