import cv2
import numpy as np

vid = cv2.VideoCapture(0)
# 3 == width
# 4 == height
# 10 == brightness

# vid.set(3, 640)
# vid.set(4, 480)
vid.set(10, 140)

myColors = [[5, 107, 0, 19, 255, 255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]


def findColor(img,my_colors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in my_colors:
        lower = np.array(color[0][0:3]) # h_min, s_min, v_min
        upper = np.array(color[0][3:6]) # h_max, s_max, v_max
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0])+" img", mask)




while True:
    success, img = vid.read()
    findColor(img, myColors)
    cv2.imshow("video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
