import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

source = cv.imread("samples/elon-musk.webp", cv.IMREAD_GRAYSCALE)


# ksize specifies the size of kernel aka convolution matrix.
sobelx = cv.Sobel(source, cv.CV_64F, 1, 0, ksize=-1)
sobelx2 = cv.Sobel(source, cv.CV_32F, 1, 0, ksize=-1)
sobelx3 = cv.Sobel(source, cv.CV_16S, 1, 0, ksize=-1)
sobelx4 = cv.Sobel(source, cv.CV_8U, 1, 0, ksize=-1)

sobely = cv.Sobel(source, cv.CV_64F, 0, 1, ksize=7)

laplacian = cv.Laplacian(source, cv.CV_64F)

cv.imshow("Original image", source)
cv.imshow("Sobel-x Derivative", sobelx)
cv.imshow("Sobel-x2 Derivative", sobelx2)
cv.imshow("Sobel-x3 Derivative", sobelx3)
cv.imshow("Sobel-x4 Derivative", sobelx4)

# cv.imshow("Sobel-y Derivative", sobely)
# cv.imshow("Laplacian Derivative", laplacian)

cv.waitKey(0)
cv.destroyAllWindows()

# plt.subplot(2,2,1),plt.imshow(source)
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian)
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx)
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely)
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
 
# plt.show()