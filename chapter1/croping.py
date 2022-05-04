import cv2


img = cv2.imread("../assets/person.png")
print(img.shape)

imgResize = cv2.resize(img, (300,350))
print(imgResize.shape)

imgCropped = img[0:300,150:500]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)