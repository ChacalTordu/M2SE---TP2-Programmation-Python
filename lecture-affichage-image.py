from ast import For
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import random

#-------------------------------------------------------------------
#-------------------------------EXO 1-------------------------------
#-------------------------------------------------------------------

#Question 1
image_RGB = Image.open('mola'+'.bmp')
plt.imshow(image_RGB)
plt.show()

#Question 2
array_RGB = np.array(image_RGB)

#Question 3
image_gris = image_RGB.convert('L') 
plt.imshow(image_gris)
plt.show()

#-------------------------------------------------------------------
#-------------------------------EXO 2-------------------------------
#-------------------------------------------------------------------

#Question 1-2
fig = plt.figure(figsize=(10, 7)) # creation figure
rows = 2
columns = 2

image_test = array_RGB[:,:,1] #enlever les niveaux de couleurs
fig.add_subplot(rows, columns, 1)
plt.imshow(image_test)
plt.show()

image_test = array_RGB[:,:,2] #enlever les niveaux de couleurs
fig.add_subplot(rows, columns, 2)
plt.imshow(image_test)
plt.show()

random.randrange(0,255)