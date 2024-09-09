import cv2 as cv
import numpy as np


# source = cv.imread("samples/rectangle-box.jpg")
# Create a blank black image
source = np.zeros((400, 400, 3), dtype="uint8")

# Draw some shapes on the image
cv.rectangle(source, (50, 50), (150, 150), (255, 255, 255), -1)  # White rectangle
cv.circle(source, (300, 100), 50, (255, 255, 255), -1)           # White circle
cv.line(source, (200, 250), (350, 350), (255, 255, 255), 5)      # White line

canvas = np.zeros_like(source)

source_grayscale = cv.cvtColor(source, cv.COLOR_BGR2GRAY)

contours, hierarchy = cv.findContours(source_grayscale, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for i in contours:
    print(i)

cv.drawContours(canvas, contours, -1, (255, 0, 0), 5)

cv.imshow("Contour shape", canvas)
cv.waitKey(0)