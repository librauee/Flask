# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:18:08 2020

@author: Administrator
"""

from flask import Flask,render_template

app = Flask(__name__)

#@app.route('/')
#def index():
#   return render_template('hello.html')

#@app.route('/hello/<user>')
#def hello_name(user):
#   return render_template('hello.html', name = user)

@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello1.html',marks=score)

if __name__ == '__main__':
   app.run()
   
   
