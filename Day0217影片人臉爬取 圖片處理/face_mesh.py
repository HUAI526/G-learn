import cv2
import mediapipe as mp
from _sqlite3 import connect

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
drawing_spec1 = mp_drawing.DrawingSpec(color = (0,255,0), thickness=1, circle_radius=1)
drawing_spec2 = mp_drawing.DrawingSpec(color = (0,0,255), thickness=1, circle_radius=1)

face_mesh = mp_face_mesh.FaceMesh(max_num_faces=10, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap=cv2.VideoCapture(0)
while(cap.isOpended()):
    success, frame=cap.read()
    if success:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)
        if results.multi_face_landmarks:
            for id, face_landmarks in enumerate(results.multi_face_landmarks):
                if id%2 == 0:
                    mp_drawing.draw_landmarks(
                        image=frame, 
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACE_CONNECTIONS,
                        landmark_drawing_spec=drawing_spec1,
                        connection_drawing_spec=drawing_spec1)
                else:
                    mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACE_CONNECTIONS,
                        landmark_drawing_spec=drawing_spec2,
                        connection_drawing_spec=drawing_spec2)
        cv2.imshow('Lin JJ', frame)
        if cv2.waitKey(100) & 0xff==27:
             break
    else:
        continue
cap.release()
cv2.destroyAllWindows()       