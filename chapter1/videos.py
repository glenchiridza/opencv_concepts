import cv2

vid = cv2.VideoCapture("../assets/vid.mp4")

while True:
    success,img = vid.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

