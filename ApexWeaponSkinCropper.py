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

    # Skips non-PNG files
    if not filename.endswith(".png"):
        continue

    img = Image.open(filename)

    # 30-30 Repeater
    if filename.endswith("30-30 Repeater.png"):
        img2 = img.crop((930, 220, 930 + legendW, 220 + legendH))
        img2.save(filename)

    # Alternator SMG
    if filename.endswith("Alternator SMG.png"):
        continue

    # Bocek Compound Bow
    if filename.endswith("Bocek.png"):
        continue

    # C.A.R. SMG
    if filename.endswith("CAR.png"):
        continue

    # Charge Rifle
    if filename.endswith("Charge Rifle.png"):
        continue

    # Devotion LMG
    if filename.endswith("Devotion.png"):
        continue

    # Hemlok Burst AR
    if filename.endswith("Hemlok.png"):
        continue

    # L-STAR EMG
    if filename.endswith("L-STAR.png"):
        continue

    # Prowler Burst PDW
    if filename.endswith("Prowler.png"):
        continue

    # Rampage LMG
    if filename.endswith("Rampage.png"):
        continue

    # RE-45 Auto
    if filename.endswith("RE-45.png"):
        continue

    # R-99 SMG
    if filename.endswith("R-99.png"):
        continue

    # M600 Spitfire
    if filename.endswith("Spitfire.png"):
        continue

    # Volt SMG
    if filename.endswith("Volt.png"):
        continue

    # All other weapons
    # HAVOC Rifle, VK-47 Flatline, R-301 Carbine, Nemesis Burst AR, G7 Scout, Triple Take, Longbow DMR, Kraber .50-Cal Sniper,
    # Sentinel ESR, EVA-8 Auto, Mastiff Shotgun, Mozambique Shotgun, Peacekeeper, P2020, Wingman
    if filename.endswith("Havoc.png") or filename.endswith("Flatline.png") or filename.endswith("R-301.png") or filename.endswith("Nemesis.png") or filename.endswith("G7 Scout.png") or filename.endswith("Triple Take.png") or filename.endswith("Longbow.png") or filename.endswith("Kraber.png") or filename.endswith("Sentinel.png") or filename.endswith("EVA-8.png") or filename.endswith("Mastiff.png") or filename.endswith("Mozambique.png") or filename.endswith("Peacekeeper.png") or filename.endswith("P2020.png") or filename.endswith("Wingman.png"):
        continue

    # All other images
    else:
        continue

    image_count = image_count + 1
    print(str(image_count) + " | Cropped " + filename)

print("Cropped " + str(image_count) + " images.")
    