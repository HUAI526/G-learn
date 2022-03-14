from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import dlib
import cv2

def moutthratio(mouth):
    hight1 = np.linalg.norm(mouth[2] - mouth[9])
    hight2 = np.linalg.norm(mouth[4] - mouth[7])
    width = np.linalg.norm(mouth[0] - mouth[6])
    ratio = (hight1 + hight2) / (2.0 * width)
    return ratio

vs = VideoStream(src=0).start()
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
while True:
    frame = vs.read()
    if frame is not None:
        frame = imutils.resize(frame, width=450)
        rects = detector(frame, 0)
        for rect in rects:
            shape = predictor(frame, rect)
            shape = face_utils.shape_to_np(shape)
            mouth = shape[mStart:mEnd]
            ratio = mouthratio(mouth)
            mouth_hull = cv2.convexHull(mouth)
            cv2.drawContours(frame, [mouth_hull], -1, (0, 255, 0), 1)
            if ratio > 0.5:
                cv2.drawContours(frame, "Mouth is open!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "ratio: {:.2f}".format(ratio), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
         
        cv2.imshow("Frame", frame)
        if cv2.waitKey(10) == 27: break

cv2.destroyAllWindows()
vs.stop()   