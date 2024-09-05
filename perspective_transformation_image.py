import numpy as np 
import cv2 as cv

img = cv.imread("samples/sudoku.png")

rows, cols, ch = img.shape
pts1 = np.float32([[73, 86], [489, 70], [37, 514], [519, 519]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

perspective_matrix = cv.getPerspectiveTransform(pts1, pts2)

output = cv.warpPerspective(img, perspective_matrix, (300, 300))

cv.imshow("Original", img)
cv.imshow("Processed", output)

cv.waitKey(0)
cv.destroyAllWindows()