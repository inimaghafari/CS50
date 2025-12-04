import sys
from PIL import Image, ImageOps
import os


input_file = sys.argv[1].lower()
output_file = sys.argv[2].lower()

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".jpg" or ".jpeg" or ".png"):
    sys.exit("Invalid input")
if not sys.argv[2].endswith(".jpg" or ".jpeg" or ".png"):
    sys.exit("Invalid output")

in_ext = os.path.splitext(input_file)[1].lower()
out_ext = os.path.splitext(output_file)[1].lower()

if in_ext != out_ext:
    print("Extensions do not match")



try:
    image = Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")


image = ImageOps.fit(image, shirt.size)

image.paste(shirt, mask=shirt)

image.save(output_file)
