import sqlite3
conn = sqlite3.connect('test.sqlite')

datas = [[1, 'David', '02-123456789'],
        [2, 'Lily', '02-987654321'],]
        
for data in datas:
    conn.execute("INSERT INTO contact (id, name, tel) VALUES \
                ({}, '{}', '{}')".format(data[0], data[1], data[2]))

conn.commit()
conn.close()    