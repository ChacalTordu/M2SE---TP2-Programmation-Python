from ast import For
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import random


#-------------------------------------------------------------------
#-------------------------------EXO 1-------------------------------
#-------------------------------------------------------------------

#Question 1
image_RGB = Image.open('lena'+'.jpg')
plt.imshow(image_RGB)
image_programme = Image.open('lena'+'.bmp')
plt.suptitle('Image original')
plt.imshow(image_programme)
plt.show()

#Question 2
array_RGB = np.array(image_programme)
print(np.shape(array_RGB))

#Question 3
image_gris = image_RGB.convert('L') 
image_gris = image_programme.convert('L') 
plt.suptitle('grisé')
plt.imshow(image_gris,cmap='gray')
plt.show()

#-------------------------------------------------------------------
#-------------------------------EXO 2-------------------------------
#-------------------------------------------------------------------



plt.show()
#Question 1-2-3
fig, axs = plt.subplots(1, 3, figsize=(10, 3))
fig.suptitle('Les trois images séparés')
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
nouvelle.show()
nouvelle1.show()
nouvelle2.show()
# Sauvegarde de l'image dans un nouveau fichier-image
nouvelle.save(sauvegarde)
plt.show()
nouvelle1.save(sauvegarde1)
plt.show()
nouvelle2.save(sauvegarde2)
plt.show()


#-------------------------------------------------------------------
#-------------------------------EXO 3-------------------------------
#-------------------------------------------------------------------

 
def add_noise(img):
 
    # Getting the dimensions of the image
    
     
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 100000)
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, 511)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, 511)
         
        # Color that pixel to white
        img[y_coord][x_coord] = 255
         
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300 , 100000)
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, 511)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, 511)
         
        # Color that pixel to black
        img[y_coord][x_coord] = 0
         
    return img
 

image_filtre_poivre_et_sel = add_noise(array_RGB) 
plt.imshow(image_filtre_poivre_et_sel)
plt.show()


