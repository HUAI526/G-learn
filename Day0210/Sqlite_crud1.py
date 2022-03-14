import sqlite3
conn = sqlite3.connect('test.sqlite')

sqlstr = ''' CREATE TABLE "contact" \
("id" INTEGER PRIMARY KEY NOT NULL,
"name" TEXT NOT NULL,
"tel" TEXT NOT NULL)
'''
conn.execute(sqlstr)
conn.commit()
conn.colse()