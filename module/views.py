# -*- coding: utf-8 -*-
# encoding: utf-8

import sys
import os, json
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from models import user_info,product_info,db


reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)
app.secret_key = 'timedrugs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Istuary-1118@192.168.0.110:3306/timedrugs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

'''login_manager = LoginManager()

login_manager.init_app(app)



@login_manager.user_loader
def load_user(email):
    return user_info.query.get(email)'''








@app.route('/')
@app.route('/index')
def index():

    #ip = request.remote_addr
    all_products = db.session.query(product_info.pro_name,product_info.pro_o_price).all()


    return render_template('index.html', all_products = all_products)

@app.route('/user_register')
def user_register():

    return render_template('user_register.html')


@app.route('/user_login', methods=['POST','GET'])
def user_login():
    error = None
    if request.method == 'POST':
        user_email = request.form['user_email']


        check_user = user_info.query.filter_by(email=user_email).first()
        print check_user
        #if check_user is None:
        #    flash('not user','error')
        #    return redirect(url_for('login'))
        #login_user(user_email, remember=Flase)
        return render_template('index.html')



    return render_template('user_login.html')

@app.route('/product_recommand')
def product_recommand():

    return render_template('product_recommand.html')


@app.route('/product_promotion')
def product_promotion():

    return render_template('product_promotion.html')

