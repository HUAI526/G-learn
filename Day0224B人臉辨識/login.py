from pip._vendor.distlib._backport.tarfile import TUREAD
def getFeature(imgfile):
    img = dlib.load_rgb_image(imgfile)
    dets = detector(img, 1)
    for det in dets:
        shape = sp(img, det)
        feature = facerec.compute_face_descriptor(img, shape)
        return numpy.array(feature)

def compareimage(v, filepath):
    try:
        v2 = getFeature(filepath)
        dist = numpy.linalg.norm(v-v2)
        if dist < 0.3:
            return True
        else:
            return False
    except Exception:
        print("產生錯誤,無法辨識")
        return 0
import cv2
import sqlite3
import time
from datetime import datetime
import dlib, numpy
from skimage import io

predictor_path = "shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

conn = sqlite3.connect('member.sqlite')
cursor = conn.cursor()
sqlstr = 'SELECT * FROM member'
cursor.execute(sqlstr)
rows = cursor.fetchall()
imagedict = {}
for row in rows:
    imagedict[row[0]] = 'memberPic/' + row[1]
    
timenow = time.time()
cv2.namedWindow("frame")
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    count = 5 - int(time.time() - timenow)
    ret, img = cap.read()
    if ret == True:
        imgcopy = img.copy()
        cv2.putText(imgcopy, str(count), (200,400), cv2.FONT_HERSHEY_SIMPLEX, 15, (0, 0, 255), 35)
        cv2.imshow("frame", imgcopy)
        k = cv2.waitKey(100)
        if k == ord("z") or k == ord("Z") or count == 0:
            cv2.imwrite("media/tem.jpg", img)
            break
cap.release()
cv2.destroyWindow("frame")

success = False
v = getFeature("media/tem.jpg")
for img in imagedict:
    if compareimage(v, imagedict[img]):
        print('登入成功!歡迎' + img +'!')
        success = True
        savetime = str(datetime.now().strftime('%Y-%m-%d %H-%M:%S'))
        sqlstr = 'INSERT INTO login values("{}", "{}")'.format(img, savetime)
        cursor.execute(sqlstr)
        conn.commit()
        break
if not success:
    print('登入失敗!你不是會員') 
conn.close()