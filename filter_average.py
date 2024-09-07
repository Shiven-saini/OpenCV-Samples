import cv2 as cv
import numpy as np

img = cv.imread("samples/opencv_logo.png")

kernel = np.ones((5, 5), np.float32)/25
output = cv.filter2D(img, -1, kernel)

cv.imshow("Sample image", img)
cv.imshow("Processed image", output)
cv.waitKey(0)

cv.destroyAllWindows()