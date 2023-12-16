# app.py
# Code The Web HTML-Links

from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/hello/')
def hello():
   return render_template('hello.html')

if __name__ == '__main__':
   app.run(debug = True)
