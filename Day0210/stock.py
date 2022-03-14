# -*- coding:utf-8 -*-
import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123123',charset='utf8', db='stockdb')
with conn.cursor() as cursor:
    sql = """
    CREATE TABLE IF NOT EXISTS Stock(
    證券代號 varchar(20),
    證券名稱 varchar(20),
    成交股數 varchar(20),
    成交筆數 varchar(20),
    成交金額 varchar(20),
    開盤價 varchar(20),
    最高價 varchar(20),
    最低價 varchar(20),
    收盤價 varchar(20),
    漲跌 varchar(20),
    漲跌價差 varchar(20),
    最後揭示買價 varchar(20),
    最後揭示買量 varchar(20),
    最後揭示賣價 varchar(20),
    最後揭示賣量 varchar(20),
    本益比 varchar(20)
    
    );
    """
    cursor.execute(sql)
    conn.commit()
conn.close()
print('Iswork')

