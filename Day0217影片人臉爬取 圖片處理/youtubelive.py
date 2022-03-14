import cv2
import pafy
url = 'https://www.youtube.com/watch?v=JAzRXylm3M0'
live=pafy.new(url)
stream=live.getbest(preftype='mp4')
cap=cv2.VideoCapture(stream.url)
fps=cap.get(cv2.CAP_PROP_FPS)
print('FPS:', fps)
while(True):
    success, frame=cap.read()
    if success:
        frame=cv2.resize(frame, (960,540))
        cv2.imshow('Lin JJ', frame)
        if cv2.waitKey(int(1000/fps)) & 0xff==27:
            break
cap.release()
cv2.destroyAllWindows()