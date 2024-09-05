import numpy as np
import cv2 as cv

img = cv.imread("sources/messi5.jpg", cv.IMREAD_GRAYSCALE)

rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
translated = cv.warpAffine(img, M, (cols, rows))

cv.imshow("Translated", translated)
cv.waitKey(0)