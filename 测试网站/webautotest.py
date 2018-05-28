#coding=utf-8
from flask import Flask
from flask import request
from flask import render_template
import  random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return (render_template('homepage.html'))


@app.route('/signin', methods=['GET'])
def signin_form():
    return (render_template('loginpage.html'))

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='15902127953' and request.form['password']=='123456':
        return (render_template('welcomepage.html',username=request.form['username']))
    return (render_template('loginpage.html',message='用户名验证失败'))

if __name__ == '__main__':
    app.run()


