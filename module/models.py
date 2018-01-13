# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import DateTime,Column,Integer
import datetime
db = SQLAlchemy()


class user_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(150), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    user_password = db.Column(db.String(150), unique=False, nullable=False)


class menu_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_cate_name = db.Column(db.String(150), unique=False, nullable=False)
    keyword = db.Column(db.String(150), unique=False, nullable=False)
    reserve = db.Column(db.String(150), unique=False, nullable=False)


class pro_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pro_cate_name = db.Column(db.String(100), unique=False, nullable=False)
    upper_cate = db.Column(db.String(100), unique=False, nullable=False)
    keyword = db.Column(db.String(100), unique=True, nullable=False)
    reserve = db.Column(db.String(100), unique=False, nullable=False)






class product_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pro_name = db.Column(db.String(100), unique=False, nullable=False)
    pro_brand = db.Column(db.String(100), unique=False, nullable=False)
    pro_category = db.Column(db.String(100), unique=True, nullable=False)
    pro_img = db.Column(db.String(200), unique=False, nullable=False)
    pro_description = db.Column(db.Text, unique=False, nullable=False)
    pro_o_price = db.Column(db.Float, unique=False, nullable=False)
    pro_weight = db.Column(db.Float, unique=False, nullable=False)
    pro_spec = db.Column(db.String(100), unique=False, nullable=False)
    pro_keyword = db.Column(db.String(100), unique=False, nullable=False)
    pro_code = db.Column(db.String(255), unique=False, nullable=False)
    pro_onsell = db.Column(db.Integer, unique=False, nullable=False)
    promotion_id = db.Column(db.Integer, unique=False, nullable=False)
    promotion_enabled = db.Column(db.Integer, unique=False, nullable=False)
    whole_sale = db.Column(db.Integer, unique=False, nullable=False)
    pro_recommend = db.Column(db.Integer, unique=False, nullable=False)


class pro_discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    promotion_id = db.Column(db.Text, unique=False, nullable=False)
    discount_value = db.Column(db.Integer, unique=False, nullable=False)
    pro_buy = db.Column(db.Integer, unique=True, nullable=False)
    pro_get = db.Column(db.Integer, unique=False, nullable=False)
    pro_type = db.Column(db.Integer, unique=False, nullable=False)
    dis_start_time = db.Column(db.Integer, unique=False, nullable=False)
    dis_end_time = db.Column(db.Integer, unique=False, nullable=False)
    dis_endless = db.Column(db.Integer, unique=False, nullable=False)
    dis_enabled = db.Column(db.Integer, unique=False, nullable=False)
    pro_price = db.Column(db.Float(255), unique=False, nullable=False)


