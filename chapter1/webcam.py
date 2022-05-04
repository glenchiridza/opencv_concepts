import cv2

vid = cv2.VideoCapture(0)
# 3 == width
# 4 == height
# 10 == brightness

vid.set(3,640)
vid.set(4,480)
vid.set(10,100)

while True:
    success,img = vid.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

