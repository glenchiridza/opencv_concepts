import cv2

vid = cv2.VideoCapture(0)
# 3 == width
# 4 == height
# 10 == brightness

vid.set(3,640)
vid.set(4,480)
vid.set(10,140)


def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)


while True:
    success,img = vid.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

