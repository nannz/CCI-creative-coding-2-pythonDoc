from matplotlib import pyplot as plt
import numpy as np
import math

myImage = np.zeros((240,320))  # column first

width_frequency = 3.14159/240

frequency = width_frequency * 10

for i in range(240):
    for j in range(320):
        t = math.sin(math.sqrt(i * i + j * j) * frequency)
        myImage[i,j]=t

plt.imshow(myImage, clim=(0,1),cmap="gray")
plt.imshow(myImage, interpolation="bilinear", clim=(0,1),cmap="gray")
plt.show()