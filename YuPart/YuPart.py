import pymysql,dbConfig
import pymysql.cursors

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": dbConfig.password,
    "db": "project",
    "charset": "utf8"
}

conn = pymysql.connect(**db_settings)
cursor = conn.cursor()


def returnSelection(student_id):
    command = "SELECT course_id,c_rank FROM selectcourse WHERE  student_id=%s"
    cursor.execute(command, student_id)
    return cursor.fetchall()


def updateRank(student_id, course_id, c_rank):
    try:
        command = "UPDATE selectcourse SET c_rank=%s WHERE student_id=%s AND course_id=%s"
        cursor.execute(command, (c_rank, student_id, course_id))
        conn.commit()
    except pymysql.Error as e:
        print(f"An error occurred: {e}")


def deleteSelection(student_id, course_id):
    try:
        command = "DELETE FROM selectcourse WHERE student_id=%s AND course_id=%s"
        cursor.execute(command, (student_id, course_id))
        conn.commit()
    except pymysql.Error as e:
        print(f"An error occurred: {e}")

def calcProbability(course_id):
    command = "SELECT max_people,choose_amount FROM course WHERE c_id=%s"
    cursor.execute(command, course_id)
    max_people,choose_amount=cursor.fetchone()
    if max_people>=choose_amount:
        return 1
    else:
        return max_people/choose_amount

if __name__ == "__main__":
    #updateRank(110104008, 703003001, 3)
    # deleteSelection(110104008,703003001)
    #print(returnSelection(110104008))
    print(calcProbability('703016001'))
