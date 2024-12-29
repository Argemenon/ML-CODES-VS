import numpy as np
import matplotlib.pyplot as plt
import cv2

array = np.zeros([8,8,3], dtype= np.uint8)

for i in range(0,8):
    for j in range(0,8):
        array[i,j] = (0,255,0)

# cv2.imwrite('Image.jpg', array)

print(array)

plt.imshow(array, cmap= 'Blues')

plt.show()
