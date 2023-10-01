from flask import Flask, render_template, request, redirect, url_for, session
from flask_paginate import Pagination, get_page_args
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
import datetime as dt

app = Flask(__name__)

#메인 화면
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
