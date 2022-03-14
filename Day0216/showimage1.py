import cv2
cv2.namedWindow("ShowImage1")
cv2.namedWindow("ShowImage2")

image1 = cv2.imread("./media/img01.jpg")
image2 = cv2.imread("./media/img01.jpg",0)

cv2.imshow("ShowImage1", image1)
cv2.imshow("ShowImage2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()