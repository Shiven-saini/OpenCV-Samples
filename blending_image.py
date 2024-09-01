import cv2 as cv
import numpy as np 

img1 = cv.imread("samples/left01.jpg")
assert img1 is not None, "Unable to find source of image 1."

img2 = cv.imread("samples/left02.jpg")
assert img2 is not None, "unable to find source of image 2."

img_output = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
cv.imshow("Output", img_output)
cv.waitKey(0)
cv.destroyAllWindows()