from ast import For
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import random

#-------------------------------------------------------------------
#-------------------------------EXO 1-------------------------------
#-------------------------------------------------------------------

#Question 1
image_RGB = Image.open('lena'+'.bmp')
plt.imshow(image_RGB)
plt.show()

#Question 2
array_RGB = np.array(image_RGB)
print(np.shape(array_RGB))

#Question 3
image_gris = image_RGB.convert('L') 
plt.imshow(image_gris)
plt.show()

#-------------------------------------------------------------------
#-------------------------------EXO 2-------------------------------
#-------------------------------------------------------------------

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

random.randrange(0,255)