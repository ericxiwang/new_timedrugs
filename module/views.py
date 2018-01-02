# -*- coding: utf-8 -*-
# encoding: utf-8

import sys
import os, json, sqlite3
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
#from module import app

reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    title = '好时光'
    user = 'ericwang'
    ip = request.remote_addr

    return render_template('index.html', title=title, user=user, ip =ip)

@app.route('/user_register')
def user_register():

    return render_template('user_register.html')

@app.route('/user_login')
def user_login():

    return render_template('user_login.html')

