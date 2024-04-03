import cv2

image = cv2.imread("../Images/lambo.png")

imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)

cv2.imshow("Output Gray Scale Image", imgGray)

cv2.waitKey(0)