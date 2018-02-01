# -*- coding: utf-8 -*-
# encoding: utf-8

import sys
import os, json
from flask import Flask, render_template, request, redirect, url_for, session, current_app
from flask import flash
from werkzeug.utils import secure_filename
# from models import user_info,product_info,pro_category,menu_category,db
from models import *
from flask_login import LoginManager
from shopping_cart import shopping_cart
reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)
app.secret_key = 'timedrugs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Istuary-1118@192.168.0.110:3306/timedrugs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)

my_cart = shopping_cart()
@login_manager.user_loader
def load_user(email):
    return User.get(email)


def query_nav_left():
    nav_list_1 = db.session.query(menu_category.id, menu_category.menu_cate_name).all()
    nav_list_2 = db.session.query(pro_category.upper_cate, pro_category.pro_cate_name, pro_category.id).all()

    return nav_list_1, nav_list_2


@app.route('/')
@app.route('/index')
@app.route('/index/<int:cate_id>')
def index(cate_id=None):
    if cate_id != None:

        all_products = db.session.query(product_info.pro_code,
                                        product_info.pro_name,
                                        product_info.pro_o_price,
                                        product_info.pro_img).filter_by(pro_category=cate_id).all()
        return render_template('index.html', all_products=all_products, menu_list=query_nav_left())

    else:

        all_products = db.session.query(product_info.pro_code,
                                        product_info.pro_name,
                                        product_info.pro_o_price,
                                        product_info.pro_img).all()

        return render_template('index.html', all_products=all_products, menu_list=query_nav_left())


@app.route('/user_register')
def user_register():
    return render_template('user_register.html')


@app.route('/user_login', methods=['POST', 'GET'])
def user_login():
    error = None
    if request.method == 'POST':
        user_email = request.form['user_email']
        user_password = request.form['user_password']

        check_user = user_info.query.filter_by(email=user_email).first()
        if user_password == check_user.user_password:
            session['user_email'] = user_email
            session['user_name'] = str(check_user.last_name + " " + check_user.first_name)
            flash("用户登录成功！")

            return redirect(url_for('index'))
        else:
            return render_template('user_login.html',error_code="密码错误",menu_list=query_nav_left())

    else:
        return render_template('user_login.html', menu_list=query_nav_left())
@app.route('/user_logout')
def user_logout():
    if 'user_email' in session:

        session.clear()
        return redirect(url_for('index'))






@app.route('/product_introduce/<string:pro_code>')
def product_introduce(pro_code):
    selected_product = product_info.query.filter_by(pro_code=pro_code).first()

    if selected_product.promotion_enabled == 1:
        discount_info = pro_discount.query.filter_by(promotion_id=selected_product.promotion_id).first()

    else:
        discount_info = ""

    return render_template('product_introduce.html',
                           selected_product=selected_product,
                           discount_info=discount_info,
                           menu_list=query_nav_left())


@app.route('/product_recommand')
def product_recommand():
    return render_template('product_recommand.html')


@app.route('/product_promotion')
def product_promotion():
    return render_template('product_promotion.html')

@app.route('/shopping_cart',methods=['POST','GET'])
#@app.route('/shopping_cart/<string:pro_code>',methods=['POST'])

def shopping_cart():
    if request.method == 'POST' or request.method == 'GET':
        pro_quantity = request.form['text_box']
        pro_code = request.form['pro_code']


        a = my_cart.add_item(pro_code,pro_quantity)
        print a

        return redirect(url_for('index'))
