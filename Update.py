# coding:utf-8
import pymysql
import pymysql.cursors

# 資料庫參數設定
db_settings= {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "a1031426",
    "db": "project",
    "charset": "utf8"
}
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()

def choose_amount_update(course_ID):
    command = "SELECT count(*) FROM selectcourse WHERE  course_id=%s "
    cursor.execute(command,(course_ID))
    result=cursor.fetchone()
    # print(result[0])
    conn.commit()
    command = "UPDATE course  SET choose_amount=%s WHERE  c_id=%s "
    cursor.execute(command,(int(result[0]),course_ID))
    conn.commit()