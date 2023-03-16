from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/science')
def science():
    return render_template("science.html")

@app.route('/society')
def society():
    return render_template("society.html")

if __name__ == '__main__':
    app.run(debug=True)
