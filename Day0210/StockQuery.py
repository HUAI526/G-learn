import sqlite3
conn = sqlite3.connect('stock.sqlite')
cursor = conn.cursor()
sql = "select * from stock"
cursor.execute(sql)
datas = cursor.fetchall()
print(datas)
conn.commit()
conn.close()