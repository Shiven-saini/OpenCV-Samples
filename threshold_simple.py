import cv2 as cv
import numpy as np

img = cv.imread("samples/gradient.png", cv.IMREAD_GRAYSCALE)
assert img is not None, "Sorry, unable to find the image!"

ret, thresh1 = cv.threshold(img, 127, 180, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

cv.imshow("Original image", img)
cv.imshow("Binary", thresh1)
cv.imshow("Trunc", thresh2)
cv.imshow("Zero", thresh3)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()

