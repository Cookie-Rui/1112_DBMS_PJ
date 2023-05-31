from flask import Flask 
from flask import url_for, redirect, render_template , request, flash
import configparser
import os

# 假資料
allData = [{'department':'資科系', 'course':'資料庫', 'number':10, 'isHit': True} ,
            {'department':'經濟系', 'course':'線性代數', 'number':20, 'isHit': True} , 
            {'department':'財政系', 'course':'財政', 'number':30, 'isHit': False} , 
            {'department':'中文系', 'course':'職場英文', 'number':40, 'isHit': True} , 
            {'department':'歷史系', 'course':'人文歷史', 'number':50, 'isHit': False}]

def Delete():
    global allData
    allData.pop()
    print("delete")

# Base
# 讀取Config檔案
config = configparser.ConfigParser()
config.read('Config/config.ini')

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# region Route
# 一進去 導向其他頁面
@app.route("/")
def Init():
    return redirect(url_for('PersonPost'))

# 新增資料的頁面
@app.route('/DataSubmission', methods=['GET', 'POST'])
def PersonPost():
    # 能夠提交自己選課結果, 需求 名字(不一定)科系, 課程,以及遞補序號
    # GET : 呼叫能提交資訊的頁面
    # TODO : 當'POST'時,驗證並通過MYSQL的東西提交資料 然後返回當前頁面
    return render_template('DataSubmission.html')

# 希望獲得課程是否能上的資訊
@app.route('/CourseSelectRecommendation', methods=['GET', 'POST'])
def CourseSelectRecommendation():
    # TODO : POST 根據輸入資料回傳有修這堂課的人
    if(request.method == 'POST'):
        return render_template('recommendation.html', test=allData)
    return render_template('recommendation.html')

# 你Post上來的資料
# 可以更新以及刪除
# 更新會跳到其他頁面
@app.route('/PersonalData', methods=['GET', 'POST'])
def PersonalData():
    # TODO : POST 根據輸入資料回傳有修這堂課的人
    if(request.method == 'POST'):
        return render_template('personaldata.html', test=allData)
    return render_template('personaldata.html')

# 更新資料頁面
@app.route('/PersonalData/Update', methods=['GET', 'POST'])
def Updatedata():
    if(request.method == 'POST'):
        # 這裡做資料的更新, 更新完後導向拿取資料的頁面
        # 這裡可以做個Cache, 這樣速度會快很多ˊ ˇ ˋ(非必要)
        # 要給值 
        global allData
        allData[0] = {'department':'轉生系', 'course':'高速轉生', 'number':1, 'isHit': True}
        # TODO: 這些值可以通過request.form[]取得
        return redirect(url_for('PersonalData'))
    else:
        # 發現不太優ˊ ˇ ˋ, 目前只想到  通過傳遞 學生名字或ID 與 課程名字或ID
        # 然後再進行一次查詢, 再傳值。
        userId = request.args['student_id'] # or name 看要不要名字ˊ ˇ ˋ
        courseId = request.args['course_id']
        print(userId)
        print(courseId)
        # 然後這裡根據雙Id 查資料
        # 資料不多應該很快
        the_allData = {'course': '課程喔', 'number': 100, 'isHit' : True}
        return render_template('DataUpdate.html', FormData=the_allData)

@app.route('/delete',methods=['GET', 'POST'])
def TestDelete():
    Delete()


# endregion

if __name__ == '__main__':
    # Flask Run
    app.debug = True
    app.secret_key = os.urandom(8)
    app.run()