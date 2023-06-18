import pymysql
import pymysql.cursors

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "zero7539510?",
    "db": "project",
    "charset": "utf8"
}

conn = pymysql.connect(**db_settings)
cursor = conn.cursor()

def add_student(s_name, s_id, gender, grade, major_Did, haveSecondary):
    command = "INSERT INTO Student (s_name, s_id, gender, grade, major_Did, haveSecondary) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(command, (s_name, s_id, gender, grade, major_Did, haveSecondary))
    conn.commit()

def add_teacher(t_name, t_id, t_department_id, gender):
    command = "INSERT INTO Teacher (t_name, t_id, t_department_id, gender) VALUES (%s, %s, %s, %s)"
    cursor.execute(command, (t_name, t_id, t_department_id, gender))
    conn.commit()

def add_department(d_name, d_id):
    command = "INSERT INTO Department (d_name, d_id) VALUES (%s, %s)"
    cursor.execute(command, (d_name, d_id))
    conn.commit()

def add_course(c_name, c_id, max_people, choose_amount, teacher_id, building_id, c_time, c_department_id, credit, c_type):
    command = "INSERT INTO Course (c_name, c_id, max_people, choose_amount, teacher_id, building_id, c_time, c_department_id, credit, c_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(command, (c_name, c_id, max_people, choose_amount, teacher_id, building_id, c_time, c_department_id, credit, c_type))
    conn.commit()

# call function example
# add_student("John Doe", "S001", "Male", "Freshman", "D001", 0)
# add_teacher("Jane Smith", 1001, "D002", "Female")
# add_department("Computer Science", "D001")
# add_course("Programming 101", "C001", 50, 0, 1, "270", "D56", "101", 3, "Elective")
