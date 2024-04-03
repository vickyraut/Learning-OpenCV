import cv2
import numpy as np

image = cv2.imread("../Images/cards2.jpg")


width, height = 500, 500

#pts1=np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts1=np.float32([[702, 150], [1129, 417], [286, 694], [720, 996]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix=cv2.getPerspectiveTransform(pts1, pts2)

imgOutput=cv2.warpPerspective(image,matrix, (width, height))

cv2.imshow("Output Image", imgOutput)
cv2.imshow("Original Image", image)

cv2.waitKey(0)