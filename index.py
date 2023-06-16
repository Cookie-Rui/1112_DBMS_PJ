from flask import Flask 
from flask import url_for, redirect, render_template , request, flash
from flaskext.mysql import MySQL
import static.python.Create as create
import static.python.YuPart as yupart
from static.python.Read import same_rank, course_inquire, course_print, course_all
from static.python.Update import choose_amount_update
import pymysql
import os

# 假資料
allData = [{'department':'資科系', 'course':'資料庫', 'number':10, 'isHit': True} ,
            {'department':'經濟系', 'course':'線性代數', 'number':20, 'isHit': True} , 
            {'department':'財政系', 'course':'財政', 'number':30, 'isHit': False} , 
            {'department':'中文系', 'course':'職場英文', 'number':40, 'isHit': True} , 
            {'department':'歷史系', 'course':'人文歷史', 'number':50, 'isHit': False}]

# config 
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# mysql = MySQL(app, user="root", password="zero7539510?",
#               db="project", cursorclass=pymysql.cursors.DictCursor)

# region Route
# 一進去 導向其他頁面
@app.route("/")
def Init():        
    return redirect(url_for('CourseSelectRecommendation'))

# 希望獲得課程是否能上的資訊
@app.route('/CourseSelectRecommendation', methods=['GET', 'POST'])
def CourseSelectRecommendation():
    # TODO : POST 根據輸入資料回傳有修這堂課的人
    if(request.method == 'POST'):
        return render_template('recommendation.html', test=allData)
    return render_template('recommendation.html')

# region 新增資料 Create

# 新增資料的頁面
# 新增選課
@app.route('/Create/DataSubmission', methods=['GET', 'POST'])
def CreateSelectCourse():
    if(request.method == "POST"):
        print(request.form["Person"],request.form["Course"])
        success = create.course_selection_insert(request.form["Person"], request.form["Course"], request.form["number"])
        if(not success):
            flash("沒有成功  大概吧")
            return render_template('Create/DataSubmission.html')
        return redirect(url_for("PersonalData"))
    return render_template('Create/DataSubmission.html')

# 新增課程
@app.route('/Create/Course', methods=['GET', 'POST'])
def CreateCourse():
    if(request.method == "POST"):
        success = create.add_course(request.form["course_name"], request.form["course_id"], request.form["max_people"],
                            request.form["choose_amount"], request.form["teacher_id"],request.form["building_id"],
                            request.form["c_time"], request.form["department_id"], request.form["credit"], 
                            request.form["c_type"])
        if(not success):
            flash("Not Success")
            return render_template('Create/add_course.html')
        else:
            return render_template('Read/view_courses.html', courses=course_all())
    return render_template('Create/add_course.html')

# 新增學生
@app.route('/Create/Student', methods=['GET', 'POST'])
def CreateStudent():
    if(request.method == "POST"):
        return render_template(url_for('ReadStudents'))
    return render_template('Create/add_student.html')

# endregion 

# region  讀取資料 Read

@app.route('/Read/SelectCourse', methods=['GET', 'POST'])
def PersonalData():
    if(request.method == 'POST'):
        return render_template('Read/ReadSelectCourse.html', test=yupart.returnSelection("109204039"))
    return render_template('Read/ReadSelectCourse.html', test=yupart.returnSelectionAll())

@app.route('/Read/Course', methods=['GET', 'POST'])
def ReadCourses():
    return render_template('Read/view_courses.html', courses=course_all())

@app.route('/Read/Student', methods=['GET', 'POST'])
def ReadStudents():
    return render_template('Read/view_students.html')

@app.route('/Read/Teacher', methods=['GET', 'POST'])
def ReadTeachers():
    return render_template('Read/view_teachers.html')

@app.route('/Read/Department', methods=['GET', 'POST'])
def ReadDepartments():
    return render_template('Read/view_departments.html')

# endregion

# region 更新資料Update

# 更新資料頁面
@app.route('/PersonalData/Update', methods=['GET', 'POST'])
def Updatedata():
    if(request.method == 'POST'):
        yupart.updateRank(request.form["Student_id"], request.form["Course_id"], request.form["Number"])
        # TODO: 這些值可以通過request.form[]取得
        return redirect(url_for('PersonalData'))
    else:
        userId = request.args['student_id'] # or name 看要不要名字ˊ ˇ ˋ
        courseId = request.args['course_id']
        return render_template('Update/UpdateSelectCourse.html', FormData=yupart.returnOneSelection(userId, courseId))

@app.route('/Delete/SelectCourse',methods=['GET'])
def TestDelete():
    yupart.deleteSelection(request.args['student_id'],request.args['course_id'])
    return redirect(url_for('PersonalData'))
# endregion




# endregion

if __name__ == '__main__':
    # Flask Run
    app.debug = True
    app.secret_key = os.urandom(8)
    app.run()