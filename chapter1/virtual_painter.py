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
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255]]

color_values = [
    [51, 153, 255], [255, 0, 255], [0, 255, 0]
]

points = [

]  # x, y, color_idx


def findColor(img, my_colors, color_vals):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newer_points = []
    for color in my_colors:
        lower = np.array(color[0:3])  # h_min, s_min, v_min
        upper = np.array(color[3:6])  # h_max, s_max, v_max
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, color_vals[count], cv2.FILLED)
        if x != 0 and y != 0:
            newer_points.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]) + " img", mask)
    return newer_points


def getContours(img):
    image, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # incase they are >400
    x, y, w, h = 0, 0, 0, 0
    for ct in contours:
        area = cv2.contourArea(ct)

        if area > 400:
            # image = cv2.drawContours(imgResult, ct, -1, (255, 20, 100), 3)
            perimeter = cv2.arcLength(ct, True)

            approximate = cv2.approxPolyDP(ct, 0.02 * perimeter,
                                           True)
            x, y, w, h = cv2.boundingRect(approximate)
    # we want to return the tip of our pen not of the object drawn so we do
    return x + w // 2, y


def drawOnCanvas(points, color_vals):
    for point in points:
        cv2.circle(imgResult, (point[0], point[q]), 10, color_vals[point[2]], cv2.FILLED)


while True:
    success, img = vid.read()
    imgResult = img.copy()
    new_points = findColor(img, myColors, color_values)
    if len(new_points) != 0:
        for new_p in new_points:
            points.append(new_p)
    if len(points) != 0:
        drawOnCanvas(points, color_values)
    cv2.imshow("video", imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
