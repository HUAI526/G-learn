import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123123',charset='utf8', db='stockdb')
with conn.cursor() as cursor:
    sql = """
    insert into stock (�Ҩ�N��, �Ҩ�W��, ����Ѽ�, ���浧��, ������B, �}�L��, �̰���, �̧C��, ���L��, ���^, ���^���t, �̫ᴦ�ܶR��, �̫ᴦ�ܶR�q , �̫ᴦ�ܽ��, �̫ᴦ�ܽ�q, ���q��) values 
    
    """
    cursor.execute(sql)
    conn.commit()
conn.close()