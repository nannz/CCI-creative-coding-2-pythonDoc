from matplotlib import pyplot as plt
import numpy as np
import math

myImage = np.zeros((240,320))

# This code is exactly the same as the the code from our JS and C++ examples

PI = 3.14159

width_frequency = 3.14159 / 320

frequency = width_frequency * 500#5000

for i in range(240):
    for j in range(320):
        t = math.tan(i / frequency) * math.cos(j / frequency) + math.atan(j / frequency) * math.cos(i / frequency)
        myImage[i,j]=t

plt.imshow(myImage, clim=(0,1),cmap="gray")
plt.imshow(myImage, interpolation="bilinear", clim=(0,1),cmap="gray")
plt.show()