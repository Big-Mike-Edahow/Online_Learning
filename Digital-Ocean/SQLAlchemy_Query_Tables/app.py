# app.py
# Flask-SQLAlchemy Query Tables

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Big Mike likes to code in Python'
db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Employee {self.firstname} {self.lastname}>'

def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        e1 = Employee(
        firstname='Steve',
        lastname='Jackson',
        email='steve@example.com',
        age=49,
        hire_date=date(2012, 3, 3),
        active=True)

        e2 = Employee(
        firstname='Jared',
        lastname='Jackson',
        email='jared@example.com',
        age=48,
        hire_date=date(2016, 6, 7),
        active=True)

        e3 = Employee(
        firstname='Mike',
        lastname='Jackson',
        email='mike@example.com',
        age=46,
        hire_date=date(2015, 9, 12),
        active=True)

        e4 = Employee(
        firstname='Gabe',
        lastname='Jackson',
        email='gabe@example.com',
        age=44,
        hire_date=date(2019, 1, 3),
        active=False)

        db.session.add(e1)
        db.session.add(e2)
        db.session.add(e3)
        db.session.add(e4)
        db.session.commit()

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    create_db()
    app.run(debug=True)

