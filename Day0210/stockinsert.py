import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123123',charset='utf8', db='stockdb')
with conn.cursor() as cursor:
    sql = """
    insert into stock (靡ㄩ腹, 靡ㄩ嘿, Θユ计, Θユ掸计, Θユ肂, 秨絃基, 程蔼基, 程基, Μ絃基, 害禴, 害禴基畉, 程处ボ禦基, 程处ボ禦秖 , 程处ボ芥基, 程处ボ芥秖, セ痲ゑ) values 
    
    """
    cursor.execute(sql)
    conn.commit()
conn.close()