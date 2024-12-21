#Import only if not previously imported
import cv2
VariableName = cv2.imread("Image Processing/Images/white.jpg",-1)     #(flag = 0 or 1 or -1)

#Import only if not previously imported

cv2.imshow("White", VariableName)
cv2.waitKey(0)
cv2.destroyAllWindows()