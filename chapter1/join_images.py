import cv2
import numpy as np

img = cv2.imread("../assets/person.png")

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)