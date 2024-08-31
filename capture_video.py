
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened() :
    print("Unable to open camera!")
    exit()

width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

print(f"{width}x{height}")

# ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
# ret2 = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

# if not ret OR ret2:
#     print("Can't set higher resolution!")
#     exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame. Exiting ...")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Video Capture', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()