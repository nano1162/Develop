from flask import Flask, render_template, request, redirect, url_for, session
from flask_paginate import Pagination, get_page_args
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
import datetime as dt
# 브랜치 분기 : branch_nano

app = Flask(__name__)
app.secret_key = 'thisisthepassword'

#메인 화면
@app.route('/')
def index():
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = "SELECT * from society_table where selecter = '공통' order by _id desc "
    cur.execute(sql)

    data_list = cur.fetchall()
        
    return render_template("index.html", data_list=data_list)

#로그인 관련 기능
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        id = request.form['id']
        password = request.form['password']
        
        db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
        cur = db.cursor()
        sql = f"SELECT ifnull(max(id), 0) id from userinfo2 where id='{id}'"
        cur.execute(sql)
        a = cur.fetchall()[0][0]
        if a == '0' :
            return render_template("login.html", message="아이디 또는 비밀번호가 잘못되었습니다!")
        else:
            sql = f"SELECT password from userinfo2 where id = '{id}'"
            cur.execute(sql)
        
            if check_password_hash(cur.fetchall()[0][0], password):
                session['id'] = id
                return redirect('/')
            else :
                return render_template("login.html", message="아이디 또는 비밀번호가 잘못되었습니다!")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":

        username = request.form['id']
        password = request.form['password']
        re_password = request.form['re-password']

        db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
        cur = db.cursor()

        if not (username and password and re_password):
            return render_template("register.html", message="입력되지 않은 정보가 있습니다.")
        elif password != re_password :
            return render_template("register.html", message="비밀번호가 다릅니다.")
        else:
            sql=f"SELECT ifnull(max(id), 0) id from userinfo2 where id=replace('{username}', ' ', '')"
            cur.execute(sql)
            a = cur.fetchall()[0][0]
            print(a)
            if a == '0':
                sql = f"insert into userinfo2 (id, password) values (replace('{username}', ' ', ''), '{generate_password_hash(password)}')"
                cur.execute(sql)
                db.commit()

                cur.close()
                db.close()

                return redirect('/')
            else :
                return render_template("register.html", message="이미 존재하는 아이디입니다.")

@app.route('/auth')
def auth():
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = f"select * from userinfo2 where id='{session['id']}'"
    cur.execute(sql)

    data_list = cur.fetchall()[0]
    
    return render_template("auth.html", data_list=data_list)

@app.route('/auth/winfo', methods=["GET", "POST"])
def wauth():
    if request.method == "GET":
        return render_template("winfo.html")
    elif request.method == "POST":
        db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
        cur = db.cursor()

        tam_a = request.form['tam_a']
        tam_b = request.form['tam_b']
        tam_c = request.form['tam_c']
        jin_a = request.form['jin_a']
        jin_b = request.form['jin_b']
        lang = request.form['lang']

        sql = f"update userinfo2 set tam_a = '{tam_a}', tam_b='{tam_b}', tam_c='{tam_c}', jin_a='{jin_a}', jin_b='{jin_b}', lang='{lang}' where id='{session['id']}'"
        cur.execute(sql)
        db.commit()

        return redirect('/auth')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# 수행평가 게시판
@app.route('/board')
def board():
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()
    try:
        sql = f"select * from userinfo2 where id='{session['id']}'"
        cur.execute(sql)

        datali = cur.fetchall()
        datali
        tam_a = datali[0][2]
        tam_b = datali[0][3]
        tam_c = datali[0][4]
        jin_a = datali[0][5]
        jin_b = datali[0][6]
        lang = datali[0][7]

        sql = f"SELECT * from society_table where (subject='{tam_a}' and selecter ='A')  or (subject = '{tam_b}' and selecter ='B') or  (subject='{tam_c}' and selecter ='C') or (subject = '{jin_a}' and selecter = 'A') or (subject='{jin_b}' and selecter ='B') or subject = '{lang}' or (selecter = '공통' and not subject ='일본어' and not subject = '중국어')order by _id desc" 
    except:
        try:
            tam_a = request.args['tam_a']
            tam_b = request.args['tam_b']
            tam_c = request.args['tam_c']
            jin_a = request.args['jin_a']
            jin_b = request.args['jin_b']
            lang = request.args['lang']
            sql = f"SELECT * from society_table where (subject='{tam_a}' and selecter ='A')  or (subject = '{tam_b}' and selecter ='B') or  (subject='{tam_c}' and selecter ='C') or (subject = '{jin_a}' and selecter = 'A') or (subject='{jin_b}' and selecter ='B') or subject = '{lang}' or (selecter = '공통' and not subject ='일본어' and not subject = '중국어')order by _id desc" 
        except:
            sql = f"SELECT * from society_table order by _id desc"

    cur.execute(sql)

    data_list = cur.fetchall()
    return render_template("board.html", data_list=data_list)

@app.route('/board/wpost', methods=['POST'])
def wpost():
    if session:
        if (session['id'] == 'admin'):
            db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
            cur = db.cursor()

            title = request.form['title']
            writer = session['id']
            context = request.form['context']
            
            # 공통인지, 진로인지, 탐구인지를 넘겨주는 날짜의 개수를 표시하는 value로 판단함
            date_c_yes = request.form['date_c_yes']
            if date_c_yes == 'yes':
                date_A = request.form['date_a']
                date_B = request.form['date_b']
                date_C = request.form['date_c'] 
            elif date_c_yes == 'one':
                date_A = request.form['date_a']
            elif date_c_yes == 'no':
                date_A = request.form['date_a']
                date_B = request.form['date_b']
            subject = request.form['subject']
            date = dt.datetime.now().strftime("%Y-%m-%d")
            if date_c_yes == "no":
                sql = f"insert into society_table (title, writer, context, date, date_d, subject, selecter) values ('{title}', '{writer}', '{context}', '{date}', datediff('{date}', '{date_A}'), '{subject}', 'A')"
                cur.execute(sql)
                db.commit()

                sql = f"insert into society_table (title, writer, context, date, date_d, subject, selecter) values ('{title}', '{writer}', '{context}', '{date}', datediff('{date}', '{date_B}'), '{subject}', 'B')"
                cur.execute(sql)
                db.commit()

                cur.close()
                db.close()
            elif date_c_yes == "one":
                sql = f"insert into society_table (title, writer, context, date, date_d, subject, selecter) values ('{title}', '{writer}', '{context}', '{date}', datediff('{date}', '{date_A}'), '{subject}', '공통')"
                cur.execute(sql)
                db.commit()

                cur.close()
                db.close()
            else:

                sql = f"insert into society_table (title, writer, context, date, date_d, subject, selecter) values ('{title}', '{writer}', '{context}', '{date}', datediff('{date}', '{date_A}'), '{subject}', 'A')"
                cur.execute(sql)
                db.commit()

                sql = f"insert into society_table (title, writer, context, date, date_d, subject, selecter) values ('{title}', '{writer}', '{context}', '{date}', datediff('{date}', '{date_B}'), '{subject}', 'B')"
                cur.execute(sql)
                db.commit()

                sql = f"insert into society_table (title, writer, context, date, date_d, subject, selecter) values ('{title}', '{writer}', '{context}', '{date}', datediff('{date}', '{date_C}'), '{subject}', 'C')"
                cur.execute(sql)
                db.commit()

                cur.close()
                db.close()
            return redirect('/board')
        else:
            return '잘못된 접근입니다! 관리자가 아닐 시에는 글을 쓸 수 없습니다.'
    else:
        return '잘못된 접근입니다! 관리자가 아니며, 비로그인시에는 글을 쓸 수 없습니다.'
    

@app.route('/board/post/<int:post_id>')
def post(post_id):

    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = f"SELECT * from society_table where _id='{post_id}'"
    cur.execute(sql)

    data_list = cur.fetchall()

    return render_template("post.html", data_list=data_list)

@app.route('/board/post/<int:post_id>/delete', methods = ["POST"])
def deletepost(post_id):
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = f"SELECT writer FROM society_table WHERE _id={post_id}"
    cur.execute(sql)

    if (not session):
        return "비정상적인 접근입니다! 해킹하지 마요~"
    elif (cur.fetchall()[0][0] != session['id']):
        if (session['id'] == 'admin'):
            sql = f"DELETE FROM society_table WHERE _id='{post_id}'"
            cur.execute(sql)

            db.commit()

            cur.close()
            db.close()

            return redirect('/board')
        else:
            return "비정상적인 접근입니다! 해킹하지 마세요~"
    else:
        sql = f"DELETE FROM society_table WHERE _id='{post_id}'"
        cur.execute(sql)

        db.commit()

        cur.close()
        db.close()

        return redirect('/board')
    
@app.route('/board/post/<int:post_id>/update', methods = ["GET", "POST"])
def updatepost(post_id):
    if request.method == "GET":
        db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
        cur = db.cursor()

        sql = f"SELECT * from society_table where _id='{post_id}'"
        cur.execute(sql)

        data_list = cur.fetchall()
        return render_template("updateform.html", id=data_list[0][0], title=data_list[0][1], writer=data_list[0][2], context=data_list[0][3], date=data_list[0][4] + dt.timedelta(days=-int(data_list[0][5])), date_d = data_list[0][5])
    elif request.method == "POST":
        db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
        cur = db.cursor()

        sql = f"SELECT * FROM society_table WHERE _id={post_id}"
        cur.execute(sql)
        datawrap = cur.fetchall()[0]
        if (not session):
            return "비정상적인 접근입니다! 해킹하지 마요~"
        elif (datawrap[2] != session['id']):
            if (session['id'] == 'admin'):
                title = request.form['title']
                context = request.form['context']
                date = datawrap[4]
                date_d = request.form['date']

                sql = f"UPDATE society_table SET title ='{title}', context = '{context}', date_d=datediff('{date}', '{date_d}') WHERE _id={post_id}"
                cur.execute(sql)

                db.commit()

                cur.close()
                db.close()

                return redirect(f'/board/post/{post_id}')
            else:
                return "비정상적인 접근입니다! 해킹하지 마세요~"
        else:
            title = request.form['title']
            context = request.form['context']
            date = datawrap[4]
            date_d = request.form['date']

            sql = f"UPDATE society_table SET title ='{title}', context = '{context}', date_d=datediff('{date}', '{date_d}') WHERE _id={post_id}"
            cur.execute(sql)

            db.commit()

            cur.close()
            db.close()

            return redirect(f'/board/post/{post_id}')

@app.route('/write')
def sociteyWrite():
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
