import sqlite3
conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()
sql = "select * from contact"
cursor.execute(sql)
datas = cursor.fetchall()
print(datas)
conn.commit()
conn.close()