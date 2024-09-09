import cv2 as cv
import numpy as np

source = cv.imread("samples/star.jpg", cv.IMREAD_GRAYSCALE)

ret, source_binary = cv.threshold(source, 127, 255, cv.THRESH_BINARY)
print(source_binary)

cv.imshow("Sample", source_binary)

contours, hierarchy = cv.findContours(source_binary, 1, 2)

# Feature-1 : Calculate centroid of the object.
M = cv.moments(contours[0])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv.circle(source_binary, (cx, cy), 1, (255, 0, 0), 1)
cv.imshow("Centroid", source_binary)

print(f"Centroid coordinates => ({cx}, {cy})")

# Feature-2 : Contour area
area = cv.contourArea(contours[0])
print("Area of the contour =>", area)

# Feature-3 : Contour Perimeter
perimeter = cv.arcLength(contours[0], True)
print("Perimeter of the contour =>", perimeter)


cv.waitKey(0)
cv.destroyAllWindows()