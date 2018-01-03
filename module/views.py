# -*- coding: utf-8 -*-
# encoding: utf-8

import sys
import os, json, sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename


reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

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

@app.route('/user_login', methods=['POST','GET'])
def user_login():
    error = None
    if request.method == 'POST':
        if request.form['user_email'] == "admin":
            session['user_email'] = request.form['user_email']
            print session
            return redirect(url_for('index'))



    return render_template('user_login.html')

@app.route('/product_recommand')
def product_recommand():

    return render_template('product_recommand.html')


@app.route('/product_promotion')
def product_promotion():

    return render_template('product_promotion.html')

