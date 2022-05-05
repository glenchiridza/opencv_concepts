import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for ct in contours:
        area = cv2.contourArea(ct)
        print(area)


path = "../assets/person.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContours(imgCanny)

imgBlank = np.zeros_like(img)
cv2.imshow("Original", img)
cv2.imshow("imgGray", imgGray)
cv2.imshow("imgBlur", imgBlur)
cv2.imshow("imgCanny", imgCanny)
cv2.imshow("imgBlank", imgBlank)
cv2.waitKey(0)
