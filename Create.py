# coding:utf-8
import pymysql
import pymysql.cursors
from function import Read
from function import Update

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



# student_ID=111501024
# c_rank=1
# same_rank(student_ID,c_rank)

def course_selection_insert(student_ID, course_ID,c_rank):
    print(Read.same_rank(student_ID,c_rank))
    if Read.same_rank(student_ID,c_rank)==True:
        return('False1')
    else:
        try:
            command = "INSERT INTO selectcourse(student_id, course_id,c_rank)VALUES(%s, %s,%s)"
            cursor.execute(command,(student_ID,course_ID,int(c_rank)))
            conn.commit()
            Update.choose_amount_update(course_ID)
            return(True)
        except:
            return ('False2')

# student_ID=111501024
# course_ID=703957001
# c_rank=5
# print(course_selection_insert(student_ID,course_ID,c_rank))



# course_ID=703837001
# choose_amount_update(course_ID)
# # conn.commit()
# command = "SELECT choose_amount FROM course WHERE  c_id=%s "
# cursor.execute(command,(course_ID))
# result=cursor.fetchone()
# print(result[0])



# course_ID=703837001
# course_inquire(course_ID)
# print(1)
# check_course='設計'
# course_inquire(check_course)
# # check_course='%'+check_course+'%'
# # command = "SELECT c_id FROM course WHERE  c_name LIKE %s "
# # cursor.execute(command,(check_course))
# # result=cursor.fetchall()
# # print(len(result))





# check_course='設計'
# course_inquire(check_course)
# course_ID=703837001
# result=course_inquire(course_ID)
# print(result)
# print(course_print(result))

