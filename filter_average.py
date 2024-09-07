import cv2 as cv
import numpy as np

img = cv.imread("samples/opencv-logo-white.png")

kernel = np.ones((3, 3), np.float32)/9
output = cv.filter2D(img, -1, kernel)

cv.imshow("Sample image", img)
cv.imshow("Processed image", output)
cv.waitKey(0)

cv.destroyAllWindows()