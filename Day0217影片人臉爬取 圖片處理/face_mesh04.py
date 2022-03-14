import cv2
import mediapipe as mp
import numpy as np
from colorama.ansi import Back
from Day0217.face_mesh import mp_drawing, mp_face_mesh, drawing_spec1

def overlay_transparent(background, overlay, overlayX, overlayY):
    background_width = background.shape[1]
    background_height = background.shape[0]
    if overlayX >= background_width or overlayY >= background_height:
        return background
    
    overlayH, overlayW = overlay.shape[0], overlay.shape[1]
    if overlayX + overlayW > background_width:
        overlayW = background_width - overlayX
        overlay = overlay[:, :overlayW]
        
    if overlayY + overlayH > background_height:
        overlayH = background_height - overlayY
        overlay = overlay[:overlayH]
        
    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1],1), dtype = overlay.dtype) * 255
            ],
            axis = 2,
        )
        
    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0
    
    background[overlayY:overlayY+overlayH, overlayX:overlayX:overlayX+overlayW] = (1.0 - mask) *\
        background[overlayY:overlayY+overlayH, overlayX:overlayX+overlayW] + mask * overlay_image
    
    return background

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
drawing_spec1 = mp_drawing.DrawingSpec(color = (0, 255, 0), thickness=1, circle_radius=1)
drawing_spec2 = mp_drawing.DrawingSpec(color = (0, 0, 255), thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(max_num_face=10, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mouth_normal = cv2.imread("./media/lips2.png", cv2.IMREAD_UNCHANGED)
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    success, frame=cap.read()
    if success:
        try:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, d = frame.shape
            results = face_mesh.process(image)
            if results.multi_face_landmarks:
                for id, face_landmarks in enumerate(results.mult_face_landmarks):
                    mouth_h = int((face_landmarks.landmark[17].y*h)-(face_landmarks.landmark[0].y*h))
                    mouth_w = int((face_landmarks.landmark[287].x*w)-(face_landmarks.landmark[57].x*w))
                    mouth = cv2.resize(mouth_normal, (mouth_w, mouth_h))
                    x, y = int(face_landmarks.landmarks[57].x*w), int(face_landmarks.landmarks[0].y*h)
                    overlay_transparent(frame, mouth,x,y)
            cv2.imshow('Lin JJ', frame)
            if cv2.waitKey(100) & 0xff==27:
                break
        except:
            pass
    else:
        continue
cap.release()
cv2.destroyAllWindows()