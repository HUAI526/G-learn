import dlib
import cv2

cnn_detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
img = cv2.imread("media\\person5.jpg")
dets = cnn_detector(img, 1)
print("人臉數:{}".format(len(dets)))
for i, det in enumerate(dets):
    face = det.rect
    left = face.left()
    top = face.top()
    right = face.right()
    bottom = face.bottom()
    print("偵測人臉{}:左:{}上:{}右:{}下:{} 信心指數:{}".format(i, left, top, right, bottom, det.confidence))
    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 1)
    
cv2.namedWindow("win", cv2.WINDOW_AUTOSIZE)
cv2.imshow("win", img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()