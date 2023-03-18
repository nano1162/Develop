from flask import Flask, render_template, request, redirect, url_for, session
from flask_paginate import Pagination, get_page_args
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'thisisthepassword'

#메인 화면
@app.route('/')
def index():
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = "SELECT * from society_table order by _id desc"
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
            sql=f"SELECT ifnull(max(id), 0) id from userinfo2 where id='{username}'"
            cur.execute(sql)
            a = cur.fetchall()[0][0]
            print(a)
            if a == '0':
                sql = f"insert into userinfo2 (id, password) values ('{username}', '{generate_password_hash(password)}')"
                cur.execute(sql)
                db.commit()

                cur.close()
                db.close()

                return redirect('/')
            else :
                return render_template("register.html", message="이미 존재하는 아이디입니다.")

@app.route('/auth')
def auth():
    return render_template("auth.html")

@app.route('/board/wpost', methods=['POST'])
def wpost():
    if request.method == 'POST':
        db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
        cur = db.cursor()

        title = request.form['title']
        writer = session['id']
        context = request.form['context']

        sql = f"insert into society_table (title, writer, context) values ('{title}', '{writer}', '{context}')"
        cur.execute(sql)
        db.commit()

        cur.close()
        db.close()


    return redirect('/board')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# 수행평가 게시판
@app.route('/board')
def society():

    
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    

    per_page = 10
    page, _, offset = get_page_args(per_page=per_page)

    cur = db.cursor()

    sql = "SELECT COUNT(*) FROM society_table;"
    cur.execute(sql)

    total = cur.fetchall()[0][0]

    sql = f"SELECT * from society_table order by _id desc limit {per_page} offset {offset};"

    cur.execute(sql)

    data_list = cur.fetchall()
    print(page, total, per_page)
    return render_template("board.html", data_list=data_list, pagination=Pagination(page=page, total=total, per_page=per_page,format_total=True), search=True)

@app.route('/board/post/<int:post_id>')
def post(post_id):

    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = f"SELECT * from society_table where _id='{post_id}'"
    cur.execute(sql)

    data_list = cur.fetchall()

    return render_template("post.html", id=data_list[0][0], title=data_list[0][1], writer=data_list[0][2], context=data_list[0][3])

@app.route('/board/post/<int:post_id>/delete', methods = ["POST"])
def deletepost(post_id):
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = f"SELECT writer FROM society_table WHERE _id={post_id}"
    cur.execute(sql)

    if (not session):
        return "비정상적인 접근입니다! 해킹하지 마세요~"
    elif (cur.fetchall() != session['id']):
        return "비정상적인 접근입니다! 해킹하지 마세요~"
    else:
        sql = f"DELETE FROM society_table WHERE _id='{post_id}'"
        cur.execute(sql)

        db.commit()

        cur.close()
        db.close()

        return redirect('/board')


@app.route('/write')
def sociteyWrite():
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
