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
def index():
    title = '好时光'
    user = 'ericwang'
    ip = request.remote_addr

    return render_template('index.html', title=title, user=user, ip =ip)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8000)

