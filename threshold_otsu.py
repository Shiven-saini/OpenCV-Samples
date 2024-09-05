import cv2 as cv
import numpy as np

img = cv.imread("samples/otsu-raw.jpeg", cv.IMREAD_GRAYSCALE)


# global simple thresholding
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

#Otsu's thresholding
ret, th2 = cv.threshold(img, 0, 25, cv.THRESH_BINARY+cv.THRESH_OTSU)


cv.imshow("Original Image", img)
cv.imshow("Simple threshold", th1)
cv.imshow("Otsu's processed", th2)


cv.waitKey(0)
cv.destroyAllWindows()

