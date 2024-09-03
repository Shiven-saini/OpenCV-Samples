import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened() :
    print("Unable to launch camera!")
    exit()

while 1:
    _, frame_BGR  = cap.read()

    frame_HSV = cv.cvtColor(frame_BGR, cv.COLOR_BGR2HSV)

    # Defining HSV Bounds to gather.
    lower_bound = np.array([170, 150, 50])
    upper_bound = np.array([180, 255, 255])

    # frame data only in the given bound
    mask = cv.inRange(frame_HSV, lower_bound, upper_bound)

    result = cv.bitwise_and(frame_BGR, frame_BGR, mask=mask)

    cv.imshow("Video raw", frame_BGR)
    cv.imshow("Mask", mask)
    # cv.imshow("Result", result)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

