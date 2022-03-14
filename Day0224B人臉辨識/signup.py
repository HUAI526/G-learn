import cv2 
import sqlite3

conn = sqlite3.connect('member.sqlite')
cursor = conn.cursor()
sqlstr = 'SELECT * FROM member'
cursor.execute(sqlstr)
rows = cursor.fetchall()
member = []
for row in rows:
    member.append(row[0])
while True:
    memberid = input('輸入帳號(直接按[Enter]結束:')
    if memberid == '':
        break
    elif memberid in member:
        print('此帳號已存在,不可重複')
    else:
        picfile = memberid + '.jpg'
        member.append(memberid)
        cv2.namedWindow("frame")
        cap = cv2.VideoCapture(0)
        while(cap.isOpened()):
            ret, img = cap.read()
            if ret == True:
                cv2.imshow("frame", img)
                k = cv2.waitKey(100)
                if k == ord("z") or k ==ord("z"):
                    cv2.imwrite('memberPic/' + picfile, img)
                    break
        cap.release()
        cv2.destroyWindow("frame")
        sqlstr = 'INSERT INTO member values("{}","{}")'.format(memberid, picfile)
        cursor.execute(sqlstr)
        conn.commit()
        print('帳號建立成功')
        
conn.close()