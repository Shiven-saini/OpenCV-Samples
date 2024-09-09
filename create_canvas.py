import cv2 as cv
import numpy as np

source = cv.imread("samples/messi5.jpg")

# black canvas of the same dimension as source.
canvas = np.zeros_like(source)
cv.imshow("Canvas", canvas)

if cv.waitKey(0) == ord('q') & 0xFF:
    cv.destroyAllWindows()
