import cv2

img1 = cv2.imread("DN1/image1.jpg")
img2 = cv2.imread("DN1/image2.jpg")

img1= cv2.resize(img1, (200,200))
img2= cv2.resize(img2, (200,200))
img3 = cv2.add(img1, img2)

img4 = cv2.subtract(img3,img2)

cv2.imshow("img1", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()