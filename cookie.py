# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:42:56 2020

@author: Administrator
"""

from flask import Flask,render_template,request,make_response
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index1.html")

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
       user = request.form['nm']
   
       resp = make_response(render_template('readcookie.html'))
       resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return "<h1>welcome '&plus;{}&plus;'</h1>".format(name)

if __name__ == '__main__':
   app.run()