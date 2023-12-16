# app.py
# Flask Employee Info App

from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'live your life'

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/employee/')
def employee():
   return render_template('employee.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            zip = request.form['zip']
            wage = request.form['wage']
         
            with sql.connect("database.db") as con:
                cur = con.cursor()
            
                cur.execute("INSERT INTO employees (name, address, city, state, zip, wage) VALUES (?,?,?,?,?,?)", (name, address, city, state, zip, wage))
            
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
   cur.execute("SELECT * FROM employees")
   
   rows = cur.fetchall();

   return render_template("list.html",rows = rows)

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug = True)
