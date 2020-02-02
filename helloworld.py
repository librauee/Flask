# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:26:53 2020

@author: Administrator
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello World'

if __name__=='__main__':
    app.run()