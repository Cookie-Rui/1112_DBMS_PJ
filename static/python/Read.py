# coding:utf-8
import pymysql
import pymysql.cursors
# import Update
from static.python import Update
# ��Ʈw�ѼƳ]�w
db_settings= {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "zero7539510?",
    "db": "project",
    "charset": "utf8"
}
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()

# 根據 student Id 跟 c_rank ??
def same_rank(student_ID,c_rank):
    c_rank=int(c_rank)
    command = "SELECT student_id FROM selectcourse WHERE  student_id=%s and c_rank=%s"
    try:
        cursor.execute(command,(student_ID,int(c_rank)))
        results = list(cursor.fetchone())
        return(True)
    except :
        return(False)

def course_all():
    command = "SELECT * FROM course"
    cursor.execute(command)
    results=cursor.fetchall()
    results2=[]
    for result in results:
        result=course_print(result)
        results2.append(result)
    return results2

# 根據ID 或 課程名 尋找課程
# 根據ID.  : 應該是回傳一個課程而已
# 根據名字 : 回傳相似名字的課程 
def course_inquire(check_course):
    results=[]
    if type(check_course)==int:
        Update.choose_amount_update(check_course)
        command = "SELECT * FROM course WHERE  c_id=%s "
        cursor.execute(command,(check_course))
        results=cursor.fetchone()
        return(results)
    if type(check_course)==str:
        check_course='%'+check_course+'%'
        command = "SELECT c_id FROM course WHERE  c_name LIKE %s "
        cursor.execute(command,(check_course))
        results=cursor.fetchall()
        results2=[]
        for i in range(0,len(results)):
            Update.choose_amount_update(results[i][0])
            command = "SELECT * FROM course WHERE  c_id=%s "
            cursor.execute(command,(results[i][0]))
            results2.append(cursor.fetchone())
        return(results2)

# 根據獲取的課程 利用Join Teacher 再次回傳新資料
def course_print(course):
    command = "SELECT t_name FROM teacher WHERE  t_id=%s "
    cursor.execute(command,(course[4]))
    result=cursor.fetchone()
    command = "SELECT b_name FROM building WHERE  b_id=%s "
    cursor.execute(command,(course[5]))
    result2=cursor.fetchone()
    command = "SELECT d_name FROM department WHERE  d_id=%s "
    cursor.execute(command,(course[7]))
    result3=cursor.fetchone()
    new_course=(course[0],course[1],course[2],course[3],result[0],result2[0],course[6],result3[0],course[8],course[9])
    return(new_course)