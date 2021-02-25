from matplotlib import pyplot as plt
import numpy as np
import math
#为什么debug可以跑，run不可以

myImage = np.zeros((10,10))

# change the color to 1(white) at position (5,5)
myImage[5,5]=1

plt.imshow(myImage, cmap="gray", clim=(0, 1) )
plt.show()