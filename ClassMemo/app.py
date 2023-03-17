from flask import Flask, render_template, request, redirect, url_for
import pymysql



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    if request.method == "GET":
        return render_template("login.html")
    # elif request.method == "POST":
        

@app.route('/register')
def register():
    if request.method == "GET":
        return render_template("register.html")
    ''' elif request.method == "POST":

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif password != re_password :
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            print('가입 완료! 아이디와 비밀번호는 저장되지 않았습니다 - Test Build')

        return render_template('login.html') '''

@app.route('/science')
def science():
    return render_template("science.html")

@app.route('/board/wpost', methods=['POST'])
def sowritepost():
    if request.method == 'POST':
        db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
        cur = db.cursor()

        title = request.form['title']
        writer = request.form['writer']
        context = request.form['context']

        sql = f"insert into society_table (title, writer, context) values ('{title}', '{writer}', '{context}')"
        cur.execute(sql)
        db.commit()

        cur.close()
        db.close()


    return redirect('/board')

@app.route('/board')
def society():
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = "SELECT * from society_table"
    cur.execute(sql)

    data_list = cur.fetchall()
        
    return render_template("board.html", data_list=data_list)
    
@app.route('/test')
def test():
    return render_template("gul.html")

@app.route('/board/post/<int:post_id>')
def post(post_id):

    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = f"SELECT * from society_table where _id='{post_id}'"
    cur.execute(sql)

    data_list = cur.fetchall()

    return render_template("post.html", id=data_list[0][0], title=data_list[0][1], writer=data_list[0][2], context=data_list[0][3])

@app.route('/board/post/<int:post_id>/delete')
def deletepost(post_id):
    db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
    cur = db.cursor()

    sql = f"DELETE FROM society_table WHERE _id='{post_id}'"
    cur.execute(sql)

    db.commit()

    sql = f"SELECT * from society_table where _id='{post_id}'"
    cur.execute(sql)

    cur.close()
    db.close()

    return redirect('/society')


@app.route('/write')
def sociteyWrite():
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
