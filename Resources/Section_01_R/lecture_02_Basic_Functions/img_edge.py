import cv2

image = cv2.imread("../Images/documentscanner2.jpg")

#Setting the Threshold Values
t_lower=400
t_higher=500

# Apply Canny Edge Detector

edge=cv2.Canny(image, t_lower, t_higher)

cv2.imshow("Original Image", image)

cv2.imshow("Canny Image", edge)

cv2.waitKey(0)

