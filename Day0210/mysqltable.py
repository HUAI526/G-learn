import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123123',charset='utf8', db='pythondb')
with conn.cursor() as cursor:
    sql = """
    CREATE TABLE IF NOT EXISTS Scores(
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name varchar(20),
    Chinese int(3),
    English int(3),
    Math int(3)
    );
    """
    cursor.execute(sql)
    conn.commit()
conn.close()
print('Iswork')