import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123123',charset='utf8', db='pythondb')
with conn.cursor() as cursor:
    sql = "update scores set Chinese =98 where ID = 4"
    cursor.execute(sql)
    conn.commit()
    sql = "select * from scores where ID = 4"
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
conn.close()