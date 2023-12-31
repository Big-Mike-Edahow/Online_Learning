# app.py
# Flask Student Info App

from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/student/')
def student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            zip = request.form['zip']
         
            with sql.connect("database.db") as con:
                cur = con.cursor()
            
                cur.execute("INSERT INTO students (name, address, city, zip) VALUES (?,?,?,?)", (name, address, city, zip))
            
                con.commit()
                msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"
      
        finally:
            return render_template("result.html",msg = msg)
            con.close()

@app.route('/list/')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();

   return render_template("list.html",rows = rows)

@app.route('/about')
def about():
   return render_template('about.html')

if __name__ == '__main__':
   app.run(debug = True)
