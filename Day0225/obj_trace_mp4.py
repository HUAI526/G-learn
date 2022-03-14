import dlib
import cv2


def onMouseClicked(event, x, y, flags, param):
    global selection, track_window, drag_start
    if event == cv2.EVENT_LBUTTONDOWN:
        drag_start = (x, y)
        track_window = None
    if drag_start:
        xMin = min(x, drag_start[0])
        yMin = min(y, drag_start[1])
        xMax = max(x, drag_start[0])
        yMax = max(y, drag_start[1])
        selection = (xMin, yMin, xMax, yMax)
    if event == cv2.EVENT_LBUTTONUP:
        drag_start = None
        track_window = selection
        selection = None
 
tracker = dlib.correlation_tracker()
cap = cv2.VideoCapture('media\\person2.mp4')
start_flag = True
selection = None
track_window = None
track_start = None
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback("image", onMouseClicked)

while(True):
    ret, frame = cap.read()
    if type(frame) != type(None):
        if start_flag == True:
            while True:
                img_first = frame.copy()
                if track_window:
                    cv2.rectangle(img_first, (track_window[0], track_window[1]), (track_window[2], track_window[3]), (0, 0, 255), 1)
                elif selection:
                    cv2.rectangle(img_first, (selection[0], selection[1]), (selection[2], selection[3]), (0, 0, 255), 1)
                cv2.imshow("image", img_first)
                if cv2.waitKey(5) == 13:
                    break
            start_flag=False
            tracker.start_track(frame, dlib.rectangle(track_window[0], track_window[1], track_window[2], track_window[3]))
        else:
            tracker.update(frame)
            box_predict = tracker.get_postion()
            cv2.rectangle(frame, (int(box_predict.left()), int(box_predict.top())), (int(box_predict.right()),int(box_predict.bottom())),(0,255,255),1)
            cv2.imshow("image", frame)
            if cv2.waitKey(10) == 27: break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()             