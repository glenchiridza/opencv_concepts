import cv2
import numpy as np


def getContours(img):
    image, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for ct in contours:
        area = cv2.contourArea(ct)
        print(area)
        image = cv2.drawContours(imgContour, ct, -1, (255, 20, 0),
                         3)  # -1 contour index, hence -1 means to draw all the contours
        if area > 400:
            image = cv2.drawContours(imgContour, ct, -1, (255, 20, 100),3)
            # calculate curve length to approximate the corners of our shape
            perimeter = cv2.arcLength(ct,True) # True meaning it is closed


    return image


path = "../assets/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

imgCont = getContours(imgCanny)

imgBlank = np.zeros_like(img)
cv2.imshow("Original", img)
cv2.imshow("imgGray", imgGray)
cv2.imshow("imgBlur", imgBlur)
cv2.imshow("imgCanny", imgCanny)
cv2.imshow("imgBlank", imgBlank)
cv2.imshow("imgCont", imgCont)
cv2.waitKey(0)
