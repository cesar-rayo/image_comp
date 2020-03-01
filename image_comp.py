from PIL import Image, ImageChops

i1 = Image.open("./input_1/image.jpg")
i2 = Image.open("./input_2/image.jpg")

diff = ImageChops.difference(i1, i2)

if diff.getbbox():
    diff.save("./output/difference.jpg")
