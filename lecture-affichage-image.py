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

#Question 2
array_RGB = np.array(image_programme)
print(np.shape(array_RGB))

#Question 3
image_gris = image_programme.convert('L') 
plt.suptitle('grisé')
plt.imshow(image_gris,cmap='gray')

#-------------------------------------------------------------------
#-------------------------------EXO 2-------------------------------
#-------------------------------------------------------------------

# Nom du fichier-image original
base = "lena.bmp"
# Nom du fichier-image modifié
sauvegarde = "modification_filtrerouge.bmp"
sauvegarde1 = "modification_filtrevert.bmp"
sauvegarde2 = "modification_filtrebleu.bmp"

def modifier_image(nom , filtrage) :
    '''Fonction qui renvoie un objet-image après l'avoir filtrer pixel par pixel'''
    # Création de l'objet-image propre à Python
    ref_image = Image.open(nom)
 
    # Lecture et action sur les pixels, un par un
    largeur, hauteur = ref_image.size
    for x in range(largeur) :
        for y in range(hauteur) :
            # On récupère les valeurs RGB du pixel de coordonnées (x,y)
            rouge, vert, bleu = ref_image.getpixel( (x,y) )
            # On transforme les valeurs RGB avec la fonction de filtrage
            rouge, vert, bleu = fonction_filtrage(rouge,vert,bleu,filtrage)
            # On transforme l'image-Python en mémoire
            ref_image.putpixel( (x, y) , (rouge, vert, bleu) )
    return ref_image
 
def fonction_filtrage(r,g,b,filtrage):
    '''Fonction qui filtre'''
    if filtrage == 0:
        red = 0
        green = g
        blue = b
    if filtrage == 1:
        red = r
        green = 0
        blue = b
    if filtrage == 2:
        red = r
        green = g
        blue = 0
    return (red, green, blue)

# Création d'une nouvelle image à partir de la source originale, type de filtrage
nouvelle = modifier_image(base , 0)
nouvelle1 = modifier_image(base , 1)
nouvelle2 = modifier_image(base , 2)
 
# Affichage de l'objet-image Python à l'écran
#nouvelle.show()
#nouvelle1.show()
#nouvelle2.show()
# Sauvegarde de l'image dans un nouveau fichier-image
nouvelle.save(sauvegarde)
nouvelle1.save(sauvegarde1)
nouvelle2.save(sauvegarde2)


#Inversion couleur negatife à positife
im = np.array(Image.open('lena.bmp'))
image_inverse = 255 - im
# Sauvegarde de l'image inversé dans un nouveau fichier image
Image.fromarray(image_inverse).save('lena_inverse.jpg')

