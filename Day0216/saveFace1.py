import cv2

casc_path = cv2.data.haarcascades + "haarcascades_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)
imagename = "./media/personl.jpg"
image = cv2.imread(imagename)
faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
count = 1
for (x,y,w,h) in faces:
    filename = "./media/face" + str(count)+ ".jpg"
    image1 = image[y:y + h, x: x + w]
    image2 = cv2.resize(image1, (400,400))
    cv2.imwrite(filename, image2)
    count += 1
    cv2.rectangle(image, (x,y), (x+w,y+h), (128,255,0), 2)
cv2.namedWindow("facedetect")
cv2.imshow("facedetect", image)
cv2.waitKey(0)
cv2.destroyWindow("facedetect")