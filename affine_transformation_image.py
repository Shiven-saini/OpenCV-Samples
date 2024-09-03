import cv2 as cv
import numpy as np

img = cv.imread("samples/home.jpg")
assert img is not None, "Unable to find this file in the samples directory provided!"

rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

affine_matrix = cv.getAffineTransform(pts1, pts2)
output = cv.warpAffine(img, affine_matrix, (cols, rows))

cv.imshow("Original", img)
cv.imshow("Processed", output)
cv.waitKey(0)
cv.destroyAllWindows()