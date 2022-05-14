import cv2
import numpy as np


def getContours(img):
    image, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for ct in contours:
        area = cv2.contourArea(ct)
        print(area)
        # image = cv2.drawContours(imgContour, ct, -1, (255, 20, 0),
        #                          3)  # -1 contour index, hence -1 means to draw all the contours
        # if all our images have a pixel greater than 400
        if area > 400:
            image = cv2.drawContours(imgContour, ct, -1, (255, 20, 100), 3)
            # calculate curve length to approximate the corners of our shape
            perimeter = cv2.arcLength(ct, True)  # True meaning it is closed, (all our shapes are closed
            print(perimeter)
            approximate = cv2.approxPolyDP(ct, 0.02 * perimeter,
                                           True)  # 0.02 * perimeter is for resolution, tweak to best fit
            # or maximum distance between the approximation of contour shape of the input polygon vs hte origin shape
            print(approximate)  # gives the corner points of each of the shapes
            print(len(approximate))
            objCorners = len(approximate)

            # from the bounding box we can get the total width,height,centerwidth of the object
            x, y, w, h = cv2.boundingRect(approximate)
            # note that we can detect from the len(approximate) that 3 means triange, 4 means squarer or rectange, etc
            if objCorners == 3: object_type = "Tri"
            else: object_type = "None"
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, object_type, \
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_PLAIN, 0.6,
                        (0, 0, 0),
                        2)  # x+(w//2)-10 , y+(h//2) to get the center point of x and y which results in  the center
            # point coordinate(x,y)

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
