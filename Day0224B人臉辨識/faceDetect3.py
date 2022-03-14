import numpy as np
import cv2
import dlib

predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()

img = cv2.imread("media\\bear1.jpg")
dets = detector(img, 1)

for det in dets:
    landmarks=[]
    for p in predictor(img, det).parts():
        landmarks.append(np.matrix([p.x,p.y]))
        
    for idx, point in enumerate(landmarks):
        pos = (point[0, 0], point[0,1])
        cv2.circle(img, pos, 5, color=(0, 255, 0))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(idx+1), pos, font, 0.4, (0, 0, 255), 1,cv2.LINE_AA)
        
cv2.namedWindow("img", 2)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyWindow("img")