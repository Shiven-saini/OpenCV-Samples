import cv2 as cv
import numpy as np

img_source = cv.imread("samples/messi5.jpg")
assert img_source is not None, "Sorry bro! Didn't find the image source."

print(img_source.shape)

ball = img_source[280:340, 330:390]
img_source[273:333, 100:160] = ball

cv.imshow("Messi", img_source); cv.waitKey(0)
cv.destroyAllWindows()