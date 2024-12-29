import numpy as np
import matplotlib.pyplot as plt
import cv2

array = np.zeros([3,3,3], dtype= np.uint8)

array[0,0] = (1,1,1)
array[0,1] = (1,1,1)

print(array)

array[1,1] = array[0,0] + array[0,1]

print(array)
