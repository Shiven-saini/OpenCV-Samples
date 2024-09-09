import cv2 as cv 
import numpy as np 
import requests

ip_device = "100.64.42.8"
url = f"http://{ip_device}:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv.imdecode(img_arr, -1)

    source = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # frame_gaussian = cv.GaussianBlur(source, (3, 3), 1)
    frame_bilateral = cv.bilateralFilter(source, 9, 75, 75)
    edge = cv.Canny(frame_bilateral, 150, 200)

    cv.imshow("Original", source)
    cv.imshow("Edges", edge)
    # cv.imshow("Webcam", img)

    if cv.waitKey(25) == ord('q'):
        break

cv.destroyAllWindows()