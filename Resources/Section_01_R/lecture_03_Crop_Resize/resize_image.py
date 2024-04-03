import cv2

image=cv2.imread("../Images/lambo.png")

print("Original Image Shape", image.shape)
#----> 1000--> resize image widh
#---> 650 __. resize image height
image_resize=cv2.resize(image, (100, 80))
print("Resize Image Shape", image_resize.shape)

cv2.imshow("Original Image", image)

cv2.imshow("Resize Image", image_resize)

cv2.waitKey(0)