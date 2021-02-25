from matplotlib import pyplot as plt
import numpy as np
import math

myImage = np.zeros((240,320))
myImage2 = np.zeros((240,320))

# This code is exactly the same as the the code from our JS and C++ examples
centre = 100
size = 50

# distance field to draw a circle
for i in range(240):
    for j in range(320):
        x_dist = abs(centre-i)
        y_dist = abs(centre-j)
        dist = math.sqrt(x_dist * x_dist + y_dist * y_dist)
        if dist < size:
            myImage[i,j] = 1


# use built in numpy distance functions to draw a circle
centre2 = 100 #为什么该这个centre没有用？图照样画到100，100的位置。
size2 = 100 #为什么这里size2 一定要100而不是50，才会和原来的一样大
for i in range(240):
    for j in range(320):
        position=np.array([[i,j],[abs(centre2-i),abs(centre2-j)]])
        distance = np.linalg.norm(position[0:1] - position[1:2])
        if distance < size2:
            myImage[i,j] = 0.5
plt.imshow(myImage, clim=(0,1),cmap="gray")
plt.imshow(myImage, interpolation="bilinear", clim=(0,1), cmap="gray")
plt.show()

# calculate distances in high dimensions
# This is actually five times slower
# but it is easier to write if you are operating in high dimensions.
positions=np.array([[30,40],[50,60],[70,80]])
print(positions[0:1]) #[[30 40]]
print(positions[1:2]) #[[50 60]]
print(positions[2:3])
# using built in np function for normalised distance
distance = np.linalg.norm(positions[0:1] - positions[1:2])
print (distance)