import numpy as np 
import cv2 as cv 

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'x264')
out = cv.VideoWriter('processed/output.mkv', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame! Exiting ....")
        break

    out.write(frame)
    cv.imshow('Video frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()