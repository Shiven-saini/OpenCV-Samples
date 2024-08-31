import cv2 as cv
import numpy as np

# defining mouse callback function
def draw_circle(event, x,y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        #// draws a blue filled circle, when double clicked.
        cv.circle(img, (x,y), 100, (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()