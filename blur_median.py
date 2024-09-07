import cv2 as cv
import numpy as np

source = cv.imread("samples/noise.jpg")

filtered = cv.medianBlur(source, 7)

cv.imshow("Original image", source)
cv.imshow("Processed image", filtered)
cv.waitKey(0)