import numpy as np
import cv2 as cv

img = cv.imread("samples/messi5.jpg")

res = cv.resize(img, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)

cv.imshow("Original", img)
cv.imshow("Resized with Cubic Interpolation", res)
cv.waitKey(0)

cv.destroyAllWindows()