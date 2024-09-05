import cv2 as cv
import numpy as np


img = cv.imread("samples/sudoku.png", cv.IMREAD_GRAYSCALE)

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow("Original", img)
cv.imshow("Simple adaptive", th1)
cv.imshow("Mean Adaptive", th2)
cv.imshow("Gaussian Adaptive", th3)

cv.waitKey(0)

cv.destroyAllWindows()
    