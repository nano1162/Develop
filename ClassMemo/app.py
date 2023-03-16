from flask import Flask, render_template, request

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

@app.route('/society')
def society():
    return render_template("society.html")

if __name__ == '__main__':
    app.run(debug=True)
