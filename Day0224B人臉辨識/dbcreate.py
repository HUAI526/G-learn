import sqlite3

conn = sqlite3.connect('member.sqlite')
cursor = conn.cursor()
sqlstr = 'CREATE TABLE IF NOT EXISTS member("memberid" TEXT, "picture" TEXT)'
cursor.execute(sqlstr)
sqlstr = 'CREATE TABLE IF NOT EXISTS login("memberid" TEXT, "ltime" TEXT)'
cursor.execute(sqlstr)
conn.commit()

conn.close()