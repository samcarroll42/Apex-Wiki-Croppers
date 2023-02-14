import os
from PIL import Image

legendW = 546
legendH = 858
image_count = 0

# Take user input for folder path and sets as the working directory.
directory = os.fsencode(input("Type the path of the image folder to be cropped: "))
directory_name = str(directory)[2:len(str(directory)) - 1]

# Iterates through each file in the folder.
for file in os.listdir(directory):
    filename = directory_name + "\\" + str(os.fsdecode(file))
    img = Image.open(filename)

    # Ash
    if filename.endswith("Ash.png"):
        img2 = img.crop((930, 220, 930 + legendW, 220 + legendH))
        img2.save(filename)

    # Bangalore
    elif filename.endswith("Bangalore.png"):
        img2 = img.crop((931, 204, 931 + legendW, 204 + legendH))
        img2.save(filename)

    # Bloodhound
    elif filename.endswith("Bloodhound.png"):
        img2 = img.crop((930, 200, 930 + legendW, 200 + legendH))
        img2.save(filename)
    
    # Catalyst
    elif filename.endswith("Catalyst.png"):
        img2 = img.crop((930, 210, 930 + legendW, 210 + legendH))
        img2.save(filename)

    # Caustic
    elif filename.endswith("Caustic.png"):
        img2 = img.crop((920, 180, 920 + legendW, 180 + legendH))
        img2.save(filename)

    # Crypto
    elif filename.endswith("Crypto.png"):
        img2 = img.crop((930, 220, 930 + legendW, 220 + legendH))
        img2.save(filename)

    # Fuse
    elif filename.endswith("Fuse.png"):
        img2 = img.crop((933, 200, 933 + legendW, 200 + legendH))
        img2.save(filename)

    # Gibraltar
    elif filename.endswith("Gibraltar.png"):
        img2 = img.crop((930, 210, 940 + legendW, 210 + legendH))
        img2.save(filename)

    # Horizon
    elif filename.endswith("Horizon.png"):
        img2 = img.crop((933, 200, 933 + legendW, 200 + legendH))
        img2.save(filename)

    # Lifeline
    elif filename.endswith("Lifeline.png"):
        img2 = img.crop((934, 196, 934 + legendW, 196 + legendH))
        img2.save(filename)

    # Loba
    elif filename.endswith("Loba.png"):
        img2 = img.crop((930, 180, 930 + legendW, 180 + legendH))
        img2.save(filename)

    # Mad Maggie
    elif filename.endswith("Maggie.png"):
        img2 = img.crop((931, 204, 931 + legendW, 204 + legendH))
        img2.save(filename)

    # Mirage
    elif filename.endswith("Mirage.png"):
        img2 = img.crop((938, 203, 938 + legendW, 203 + legendH))
        img2.save(filename)

    # Newcastle
    elif filename.endswith("Newcastle.png"):
        img2 = img.crop((920, 176, 920 + legendW, 176 + legendH))
        img2.save(filename)

    # Octane
    elif filename.endswith("Octane.png"):
        img2 = img.crop((934, 200, 934 + legendW, 200 + legendH))
        img2.save(filename)

    # Pathfinder
    elif filename.endswith("Pathfinder.png"):
        img2 = img.crop((933, 200, 933 + legendW, 200 + legendH))
        img2.save(filename)

    # Rampart
    elif filename.endswith("Rampart.png"):
        img2 = img.crop((920, 180, 920 + legendW, 180 + legendH))
        img2.save(filename)

    # Revenant
    elif filename.endswith("Revenant.png"):
        img2 = img.crop((930, 180, 930 + legendW, 180 + legendH))
        img2.save(filename)

    # Seer
    elif filename.endswith("Seer.png"):
        img2 = img.crop((933, 200, 933 + legendW, 200 + legendH))
        img2.save(filename)

    # Valkyrie
    elif filename.endswith("Valkyrie.png"):
        img2 = img.crop((920, 180, 920 + legendW, 180 + legendH))
        img2.save(filename)

    # Vantage
    elif filename.endswith("Vantage.png"):
        img2 = img.crop((915, 185, 915 + legendW, 185 + legendH))
        img2.save(filename)

    # Wattson
    elif filename.endswith("Wattson.png"):
        img2 = img.crop((930, 220, 930 + legendW, 220 + legendH))
        img2.save(filename)

    # Wraith
    elif filename.endswith("Wraith.png"):
        img2 = img.crop((930, 220, 930 + legendW, 220 + legendH))
        img2.save(filename)

    image_count = image_count + 1
    print(str(image_count) + " | Cropped " + filename)

print("Cropped " + str(image_count) + " images.")
    