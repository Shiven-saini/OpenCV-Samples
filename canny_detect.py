import cv2 as cv
import numpy as np

source = cv.imread("samples/hand.png", cv.IMREAD_GRAYSCALE)
edges = cv.Canny(source, 80, 200)

cv.imshow("Original", source)
cv.imshow("Edges", edges)
cv.waitKey(0)

cv.destroyAllWindows()