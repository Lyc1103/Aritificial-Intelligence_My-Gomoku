# -*- coding: utf-8 -*-
from PIL import Image

img_name = input("Please intput the image name you want to mat: ")
image = Image.open(img_name)
image = image.convert('RGBA')
print(image.mode)


# Transparency
newImage = []
for item in image.getdata():
    if item[:3] == (255, 255, 255):
        newImage.append((255, 255, 255, 0))
    else:
        newImage.append(item)

image.putdata(newImage)


image.save('output.png')
print(image.mode, image.size)
print("The image has been matted.")
