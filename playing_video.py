import numpy as np 
import cv2 as cv

cap = cv.VideoCapture("samples/vtest.avi")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame! Exiting ....")
        break
    
    cv.imshow("Playing video file", frame)
    if cv.waitKey(25) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()