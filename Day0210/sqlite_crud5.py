import sqlite3
conn = sqlite3.connect('test.sqlite')

conn.execute("DELETE FROM contact WHERE id={}".format(1))
conn.commit()
conn.close()