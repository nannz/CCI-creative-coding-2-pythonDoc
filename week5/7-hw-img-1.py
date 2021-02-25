import numpy as np

from scipy.misc import imread, imresize
import imageio


import matplotlib.pyplot as plt

img = imageio.imread('assets/nan_small.jpg')  # Returns a numpy array
print(img.dtype, img.shape)  # Prints "uint8 (400, 400, 3)"
np_img = np.uint8(img)  # shape is (40,40,3)

img_test = np_img[0,0]  # the first pixel is [102,39,250]
print(img_test)

#img = imread('assets/nan.jpg')  # `imread` is deprecated in SciPy 1.0.0
img_tinted = img * [1, 0.95, 0.9]

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)

# Show the tinted image
plt.subplot(1, 2, 2)
# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. So cast the dataType to uint8
plt.imshow(np.uint8(img_tinted))  # use the imshow function to show images
plt.show()