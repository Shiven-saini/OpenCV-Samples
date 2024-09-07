import cv2 as cv
import numpy as np

source = cv.imread("samples/opencv-logo.png")

output = cv.blur(source, (3, 3))
output2 = cv.blur(source, (5, 5))

cv.imshow("3x3 matrix", output)
cv.imshow("5x5 matrix", output2)
cv.waitKey(0)

cv.destroyAllWindows()