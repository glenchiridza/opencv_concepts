import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
# img[0:150,200:400] = 255,0,0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)
cv2.rectangle(img, (0, 0), (245, 265), (255, 0, 255), 3)
cv2.rectangle(img, (245, 265), (345, 465), (255, 0, 255), cv2.FILLED)
cv2.circle(img, (400, 50), 30, (255, 255, 255), 5)
cv2.putText(img,"Hello glen",(350,100),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
cv2.imshow("Image", img)

cv2.waitKey(0)
