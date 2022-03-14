import sqlite3
conn = sqlite3.connect('test.sqlite')

conn.execute("UPDATE contact SET name='{}' WHERE id={}".format('ken',1))
conn.commit()
conn.close()