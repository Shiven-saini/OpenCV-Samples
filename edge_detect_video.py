import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(frame_gray, 50, 150)
    cv.imshow("Video capture grayscale", frame_gray)
    cv.imshow("Video capture Edges", edge)


    if cv.waitKey(25) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()