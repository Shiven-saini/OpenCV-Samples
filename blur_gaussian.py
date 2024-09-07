import cv2 as cv
import numpy as np 

source = cv.imread("samples/opencv-logo.png")

average_filter = cv.blur(source, (5, 5))
output = cv.GaussianBlur(source, (5, 5), 0)

cv.imshow("original image", source)
cv.imshow("Average filter", average_filter)
cv.imshow("Gaussian Blur", output)
cv.waitKey(0)

cv.destroyAllWindows()