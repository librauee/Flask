# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:20:30 2020

@author: Administrator
"""


from flask import Flask,request,session,url_for,redirect,render_template
app = Flask(__name__)
app.secret_key='abcd'


@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return "Logged in as {}<br><b><a href = '/logout'>click here to log out</a></b>".format(username)
   return "You are not logged in <br><a href = '/login'></b> click here to log in</b></a>"
      
@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template("index2.html")
 
   
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))
      
if __name__ == '__main__':
   app.run()