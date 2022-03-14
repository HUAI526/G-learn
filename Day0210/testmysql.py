import pymysql
conn = pymysql.connect(host='localhost',port=3306, db='sakila',\
                       user='root',password='123123',charset='utf8')
conn.close()
print('Iswork')