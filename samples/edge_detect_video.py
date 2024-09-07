import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video capture", frame)
    cv.imshow("Video capture grayscale", frame_gray)

    cv.waitKey(0)

cap.release()
cv.destroyAllWindows()