from ast import For
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import random

#-------------------------------------------------------------------
#-------------------------------EXO 1-------------------------------
#-------------------------------------------------------------------

#Question 1
image_programme = Image.open('lena'+'.bmp')
plt.suptitle('Image original')
plt.imshow(image_programme)
plt.show()

#Question 2
array_RGB = np.array(image_programme)
print(np.shape(array_RGB))

#Question 3
image_gris = image_programme.convert('L') 
plt.suptitle('grisé')
plt.imshow(image_gris,cmap='gray')
plt.show()

#-------------------------------------------------------------------
#-------------------------------EXO 2-------------------------------
#-------------------------------------------------------------------

#Question 1-2-3
fig, axs = plt.subplots(1, 3, figsize=(10, 3))
fig.suptitle('Les trois images séparés')

(largeur, hauteur)= image_programme.size
#image_programme_modified = image_programme
for i in range(2):
    for x in range(largeur):
        for y in range(hauteur):
            (rouge,vert,bleu) = image_programme.getpixel((x,y)) # Ici on traite le pixel (x,y) de l'image.
            if i==0:
                rouge = 0
            if i==1:
                vert = 0
            if i==2:
                bleu = 0
            image_programme.putpixel((x,y),(rouge,vert,bleu)) #supprime la couleur selon i
    axs[i].imshow(image_programme)
plt.show()


#-------------------------------------------------------------------
#-------------------------------EXO 3-------------------------------
#-------------------------------------------------------------------

random.randrange(0,255)