# To stack images 1. They have same size 2. Same Chanels (e.g Grayscale, RGB)

import cv2
import numpy as np

image1=cv2.imread("../Images/cards.jpg")

print("Image 1 Shape", image1.shape)
image1_resize=cv2.resize(image1, (318, 159))

image2 = cv2.imread("../Images/image2.jpg")

print("Image 2 Shape", image2.shape)
image2_grayscale=cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
imageHorizontalStack=np.hstack((image1_resize, image2))
imageVerticalStack=np.vstack((image1_resize, image2))

cv2.imshow("Horizontal Stack", imageHorizontalStack)
cv2.imshow("Vertical Stack", imageVerticalStack)

cv2.waitKey(0)