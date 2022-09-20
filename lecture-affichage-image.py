from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import random


image_RGB = Image.open('mola'+'.bmp')
plt.imshow(image_RGB)
plt.show()

array_RGB = np.array(image_RGB)
image_gris = image_RGB.convert('L') 
plt.imshow(image_gris)
plt.show()


#enlever niveau de rouge
image_test = array_RGB[:,:,1]
plt.imshow(image_test)
plt.show()

random.randrange(0,255)

#bitetest