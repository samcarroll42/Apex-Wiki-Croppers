import os
from PIL import Image

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
        img2 = img.crop((515, 400, 515 + 1200, 400 + 450))
        img2.save(filename)

    # Alternator SMG
    if filename.endswith("Alternator SMG.png"):
        img2 = img.crop((721, 334, 721 + 1049, 334 + 586))
        img2.save(filename)

    # Bocek Compound Bow
    if filename.endswith("Bocek.png"):
        img2 = img.crop((979, 177, 979 + 584, 177 + 901))
        img2.save(filename)

    # C.A.R. SMG
    if filename.endswith("CAR.png"):
        img2 = img.crop((640, 404, 640 + 1200, 404 + 450))
        img2.save(filename)

    # Charge Rifle
    if filename.endswith("Charge Rifle.png"):
        img2 = img.crop((630, 350, 630 + 1200, 350 + 500))
        img2.save(filename)

    # Devotion LMG
    if filename.endswith("Devotion.png"):
        img2 = img.crop((630, 400, 630 + 1200, 400 + 450))
        img2.save(filename)

    # Hemlok Burst AR
    if filename.endswith("Hemlok.png"):
        img2 = img.crop((640, 390, 640 + 1200, 390 + 450))
        img2.save(filename)

    # L-STAR EMG
    if filename.endswith("L-STAR.png"):
        img2 = img.crop((675, 390, 675 + 1200, 390 + 480))
        img2.save(filename)

    # Prowler Burst PDW
    if filename.endswith("Prowler.png"):
        img2 = img.crop((580, 300, 580 + 1200, 300 + 600))
        img2.save(filename)

    # Rampage LMG
    if filename.endswith("Rampage.png"):
        img2 = img.crop((530, 420, 530 + 1350, 420 + 400))
        img2.save(filename)

    # RE-45 Auto
    if filename.endswith("RE-45.png"):
        img2 = img.crop((772, 297, 772 + 933, 297 + 627))
        img2.save(filename)

    # R-99 SMG
    if filename.endswith("R-99.png"):
        img2 = img.crop((570, 400, 570 + 1250, 400 + 475))
        img2.save(filename)

    # M600 Spitfire
    if filename.endswith("Spitfire.png"):
        img2 = img.crop((630, 400, 630 + 1200, 400 + 450))
        img2.save(filename)

    # Volt SMG
    if filename.endswith("Volt.png"):
        img2 = img.crop((650, 400, 650 + 1200, 400 + 450))
        img2.save(filename)

    # All other weapons
    # HAVOC Rifle, VK-47 Flatline, R-301 Carbine, Nemesis Burst AR, G7 Scout, Triple Take, Longbow DMR, Kraber .50-Cal Sniper,
    # Sentinel ESR, EVA-8 Auto, Mastiff Shotgun, Mozambique Shotgun, Peacekeeper, P2020, Wingman
    if filename.endswith("Havoc.png") or filename.endswith("Flatline.png") or filename.endswith("R-301.png") or filename.endswith("Nemesis.png") or filename.endswith("G7 Scout.png") or filename.endswith("Triple Take.png") or filename.endswith("Longbow.png") or filename.endswith("Kraber.png") or filename.endswith("Sentinel.png") or filename.endswith("EVA-8.png") or filename.endswith("Mastiff.png") or filename.endswith("Mozambique.png") or filename.endswith("Peacekeeper.png") or filename.endswith("P2020.png") or filename.endswith("Wingman.png"):
        img2 = img.crop((640, 400, 640 + 1200, 400 + 450))
        img2.save(filename)

    # All other images
    else:
        continue

    image_count = image_count + 1
    print(str(image_count) + " | Cropped " + filename)

print("Cropped " + str(image_count) + " images.")
    