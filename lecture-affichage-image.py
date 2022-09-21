from ast import For
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import random
import numpy
import math
import imageio
from  matplotlib.pyplot import *


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
array_gris =  np.array(image_gris)


#-------------------------------------------------------------------
#-------------------------------EXO 2-------------------------------
#-------------------------------------------------------------------



plt.show()
#Question 1-2-3

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
 

def add_bruit_gaussien(image) :
    
    (red,green,blue)=image_RGB.split()
    array=numpy.array(red)
    s=array.shape 
    sigma=10
    for j in range(s[0]):
        for i in range(s[1]):
            v = int(math.floor(array[j][i]+random.gauss(0,sigma)))
            if v > 255:
                v = 255
            if v<0:
                v = 0
            array[j][i] = v
        
    return image

def convolution2D(X,H,moitie):
    s = X.shape
    py = (H.shape[0]-1)//2
    px = (H.shape[1]-1)//2
    Y = X.copy()
    if moitie:
        imax = int(s[1]//2)
    else:
        imax = s[1]-px
    for i in range(px,imax):
        for j in range(py,s[0]-py):
            somme = 0.0
            for k in range(-px,px+1):
                for l in range(-py,py+1):
                    somme += X[j+l][i+k]*H[l+py][k+px]
            Y[j][i] = somme
    return Y


red = array_RGB[:,:,0]

figure(figsize=(4,4))
X1 = red*1.0
imshow(X1,cmap='gray')

h = numpy.ones((3,3))*1.0/9
Y = convolution2D(X1,h,False)
figure(figsize=(4,4))
plt.suptitle('affichage de lena avec le filtre moyen')
plt.imshow(Y)
plt.show()








image_filtre_poivre_et_sel = add_noise(array_gris)
plt.suptitle('affichage de lena avec le filtre poivre et sel') 
plt.imshow(image_filtre_poivre_et_sel,cmap='gray')
plt.show()


image_filtre_bruit_gaussien = add_bruit_gaussien(array_gris)
plt.suptitle('affichage de lena avec le filtre avec du bruit gaussien') 
plt.imshow(image_filtre_bruit_gaussien,cmap='gray')
plt.show()

