# app.py
# Code The Web HTML-Wrapping

import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)
