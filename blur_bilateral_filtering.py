import cv2 as cv
import numpy as np

source = cv.imread("samples/mountains.png")
output = cv.bilateralFilter(source, 9, 75, 75)

cv.imshow("original image", source)
cv.imshow("Processed image", output)
cv.waitKey(0)

cv.destroyAllWindows()