#Import only if not previously imported
import cv2
import matplotlib.pyplot as plt
import numpy

img = cv2.imread('Image Processing/Images/bwdiagonal.jpg', -1)

plt.imshow(img)

plt.show()
