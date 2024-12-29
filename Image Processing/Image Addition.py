import cv2
import matplotlib.pyplot as plt
import numpy as np

#Create a new np array:
array = np.zeros([426,640,3], dtype= np.uint8)

img1 = cv2.imread('Image Processing/Images/city.jpg', -1)
img2 = cv2.imread('Image Processing/Images/space.jpg', -1)

h,w,c = img1.shape

print(h, w)

for i in range(0,h):
    for j in range(0,w):
        array[i,j] = 0.5*img1[i,j] + 0.5*img2[i,j]

print(np.max(array))

m = np.max(array)

for i in range(0,h):
    for j in range(0,w):
        array[i,j] = array[i,j] + (255-m, 255-m, 255-m)

print(np.max(array))

plt.imshow(array)

plt.show()