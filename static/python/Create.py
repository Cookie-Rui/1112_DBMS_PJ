# coding:utf-8
import pymysql
import pymysql.cursors

from static.python import Read
from static.python import Update

# 資料庫參數設定
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

# student_ID=111501024
# c_rank=1
# same_rank(student_ID,c_rank)

def course_selection_insert(student_ID, course_ID,c_rank):
    print(Read.same_rank(student_ID,c_rank))
    if Read.same_rank(student_ID,c_rank)==True:
        print("Same Rank")
        return False
    else:
        try:
            command = "INSERT INTO selectcourse(student_id, course_id,c_rank)VALUES(%s, %s,%s)"
            cursor.execute(command,(student_ID,course_ID,int(c_rank)))
            conn.commit()
            Update.choose_amount_update(course_ID)
            return True
        except:
            return False
        
def add_student(s_name, s_id, gender, grade, major_Did, haveSecondary):
    try:
        command = "INSERT INTO Student (s_name, s_id, gender, grade, major_Did, haveSecondary) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(command, (s_name, s_id, gender, grade, major_Did, haveSecondary))
        conn.commit()
        return True
    except:
        return False
def add_teacher(t_name, t_department_id, gender):
    try:
        command = "SELECT MAX(t_id) FROM teacher"
        cursor.execute(command)
        results=cursor.fetchone()
        t_id=results[0]+1
        command = "INSERT INTO Teacher (t_name, t_id, t_department_id, gender) VALUES (%s, %s, %s, %s)"
        cursor.execute(command, (t_name, t_id, t_department_id, gender))
        conn.commit()
        return True
    except:
        return False
    
def add_department(d_name, d_id):
    try:
        command = "INSERT INTO Department (d_name, d_id) VALUES (%s, %s)"
        cursor.execute(command, (d_name, d_id))
        conn.commit()
        return True
    except:
        return False
def add_course(c_name, c_id, max_people, choose_amount, teacher_id, building_id, c_time, c_department_id, credit, c_type):
    command = "INSERT INTO Course (c_name, c_id, max_people, choose_amount, teacher_id, building_id, c_time, c_department_id, credit, c_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(command, (c_name, c_id, max_people, choose_amount, teacher_id, building_id, c_time, c_department_id, credit, c_type))
        conn.commit()
        return True
    except:
        return False
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
# Read.course_inquire(course_ID)
# print(1)
# check_course='設計'
# Read.course_inquire(check_course)
# check_course='%'+check_course+'%'
# command = "SELECT c_id FROM course WHERE  c_name LIKE %s "
# cursor.execute(command,(check_course))
# result=cursor.fetchall()
# print(len(result))





# check_course='設計'
# Read.course_inquire(check_course)

# course_ID=703837001
# result=Read.course_inquire(course_ID)
# print(result)
# print(Read.course_print(result))

