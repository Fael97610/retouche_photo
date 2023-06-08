# Créé par fael.abdou, le 08/06/2023 en Python 3.7

from PIL import Image
fond = Image.open("desert2.jpeg")
img =Image.open("mat.jpg")
large, haut = img.size
fond.thumbnail((large,haut))

wab = img.getpixel((0,0))
large, haut = img.size
#vert = img.getpixel((0,0))
#print(vert)
seuil = 50
for y in range(haut):
    for x in range(large):
        r,v,b = img.getpixel((x,y))
        if wab >= (r-seuil,v-seuil,b-seuil) and wab <= (r+seuil,v+seuil,b+seuil) :
            pixel_fond = fond.getpixel((x,y))
            #print(pixel_fond)
            img.putpixel((x, y),pixel_fond)

img.show()





