from imutils.video import videostream
from imutils import face_utils
import imutils
import time
import dlib
import cv2


detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(left_Start,left_End)=face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(right_Start, right_End)=face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

vsThread=videostream(src=0).start()
time.sleep(2.0)

while True:
    frame = vsThread.read()
    frame = imutils.resize(frame, width=720)
    faces = detector(frame, 0)
    for face in faces:
        shape = predictor(frame, face)
        shape = face_utils.shape_to_np(shape)
        
        leftEye = shape[left_Start:left_End]
        rightEye = shape[right_Start:right_End]
        
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        mouth = shape[leftMouth:rightMouth]
        mouthHull = cv2.convexHull(mouth)
        cv2.drawContours(frame, [mouthHull], -1,(0, 255, 0), 1)
        
        nose = shape[leftNose:rightNose]
        noseHull=cv2.convexHull(nose)
        cv2.drawContours(frame, [noseHull], -1, (0, 255, 0), 1)
        
        jaw=shape[leftJaw:rightJaw]
        jawHull=cv2.convexHull(jaw)
        cv2.drawContours(frame, [jawHull], -1, (0, 255, 0), 1)
        
        leftEyebrow=shape[left_leftEyebrow:left_rightEyebrow]
        rightEyebrow=shape[right_leftEyebrow:right_rightEyebrow]
        leftEyebrowHull=cv2.convexHull(leftEyebrow)
        rightEyebrowHull=cv2.convexHull(rightEyebrow)
        cv2.drawContours(frame, [leftEyebrowHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyebrowHull], -1, (0, 255, 0), 1)
        
    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) == 27: break

cv2.destroyAllWindows()
vsThread.stop()