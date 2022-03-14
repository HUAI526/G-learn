from imutils.video import VideoStream
from imutils import face_utils
import imutils
import numpy as np
import time
import dlib
import cv2
import winsound

def eyesRatio(eye):
    hight1 = np.linalg.norm(eye[1] - eye[5])
    hight2 = np.linalg.norm(eye[2] - eye[4])
    width = np.linalg.norm(eye[2 - eye[4]])
    return (hight1+hight2) / (2.0*width)

eyesRatioLimit = 0
collectCount=0
collectSum=0
startCheck=False
eyesCloseCount=0
eyesOpenCount=0

detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(left_Start, left_End)=face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(right_Start, right_End)=face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

vsThread=VideoStream(src=0).start()
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
        leftEyesVal = eyesRatio(leftEye)
        rightEyesVal = eyesRatio(rightEye)
        
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        eyeRatioVal = (leftEyesVal + rightEyesVal) /2.0
        
        if collectCount<30:
            collectCount+=1
            collectSum+=eyeRatioVal
            startCheck=False
        else:
            if not startCheck:
                eyeRatioLimit=collectSum/(1.0*30)
                
        if startCheck:
            if eyeRatioVal < eyesRatioLimit:
                eyesCloseCount += 1
                eyesOpenCount = 0
                if eyesCloseCount >= 30:
                    cv2.putText(frame, "SLEEP!!!", (580, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    winsound.Beep(440, 1000)
            else:
                eyesOpenCount += 1
                if eyesOpenCount > 2:
                    eyesCloseCount = 0
            
            cv2.putText(frame, "EYES_RATIO: {:.2f}".format(eyeRatioVal), (20, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 160,0), 2)
            cv2.putText(frame, "EYES_COLSE: {}".format(eyesCloseCount), (320, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 160,0), 2)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) == 27: break
    
cv2.destroyAllWindows()
vsThread.stop()