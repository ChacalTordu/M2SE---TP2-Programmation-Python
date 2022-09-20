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

#enlever niveau de rouge
image_r = array_RGB[:,:,0]
image_g = array_RGB[:,:,1]
image_b = array_RGB[:,:,2]

image=array_RGB[:,:,1]
plt.subplot(1, 1)
plt.imshow(image)



image2=array_RGB[:,:,2]
plt.subplot(1, 2)
plt.imshow(image2)
plt.show()











plt.show()






random.randrange(0,255)

