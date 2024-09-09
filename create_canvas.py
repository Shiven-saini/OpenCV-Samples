import cv2 as cv
import numpy as np

source = cv.imread("samples/messi5.jpg")

# Black and white canvas of the same dimension as source.
canvas = np.ones_like(source)
canvas_white = canvas*255
canvas_black = canvas*0

cv.imshow("Canvas", canvas_white)
cv.imshow("Canvas black", canvas_black)

if cv.waitKey(0) == ord('q') & 0xFF:
    cv.destroyAllWindows()
