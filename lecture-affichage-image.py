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
image_test = array_RGB[:,:,3]
plt.imshow(image_test)
plt.show()

random.randrange(0,255)

