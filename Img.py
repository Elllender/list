from PIL import Image

img1 = Image.open('img1.jpg')
img2 = Image.open('img2.jpg')

size = img1.size

mas1 = []
mas2 = []

for x in range(0,size[0]):
    for y in range(0, size[1]):
        color = img1.getpixel((x,y))
        mas1.append(color)
        color2 = img2.getpixel((x,y))
        mas2.append(color2)

mas1.sort