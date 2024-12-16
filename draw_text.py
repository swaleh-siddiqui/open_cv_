import cv2 as cv
import numpy as np

# read image

img = cv.imread("images/stana2.jpg")
# cv.imshow("stana1", img)

blank = np.zeros((500, 500, 3), dtype="uint8")

# cv.imshow("blank", blank)

# paint full
blank[:] = 0,255,0
# cv.imshow("green", blank)

# paint a portion only
blank[200:300, 200:300] = 0,0,255
# cv.imshow("centre red", blank)

# draw rectangle
cv.rectangle(blank, (200, 200), (300, 300), (255,0,255), thickness=5)
# cv.imshow("rectange", blank)

# draw a circle 
cv.circle(img, (img.shape[1]//2, img.shape[0]//4), (500), (0,255,0), thickness=10)
# cv.imshow("circle", img)

# draw a line
cv.line(img, (img.shape[1]//2, img.shape[0]//4), (0,0), (0,255,0), thickness=10)
# cv.imshow("line", img)

# type text on image
cv.putText(img, "Sexy smilke", (400, 200), cv.FONT_HERSHEY_COMPLEX, 1.5, (0,0,255), thickness=2)
cv.imshow("text", img)

cv.waitKey(0)