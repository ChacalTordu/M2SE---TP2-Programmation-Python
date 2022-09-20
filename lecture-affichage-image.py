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
plt.show()

#Question 2
array_RGB = np.array(image_RGB)
print(np.shape(array_RGB))

#Question 3
image_gris = image_RGB.convert('L') 
plt.imshow(image_gris,cmap='gray')
plt.show()

#-------------------------------------------------------------------
#-------------------------------EXO 2-------------------------------
#-------------------------------------------------------------------



plt.show()
#Question 1-2-3
fig, axs = plt.subplots(1, 3, figsize=(10, 3))
fig.suptitle('Les trois images séparés')

for i in [0,1,2]:
    image_modified_color = array_RGB[:,:,i]
    axs[i].imshow(image_modified_color)
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


