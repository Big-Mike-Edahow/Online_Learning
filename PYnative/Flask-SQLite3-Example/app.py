# app.py
# Flask-SQLite3 Developers List

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/index')
def index():
    conn = get_db_connection()
    curs = conn.cursor()
	
    select_all = curs.execute("SELECT * FROM developers;").fetchall()
    conn.commit()
	
    sql_query = "SELECT sqlite_version();"
    version = curs.execute(sql_query).fetchall()
    conn.commit()
	
    conn.close()

    return render_template('index.html', version=version, select_all=select_all)

@app.route('/new_developer')
def new_developer():
    return render_template('new-developer.html')

@app.route('/add-developer', methods=['GET', 'POST'])
def add_developer():
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		joining_date = request.form.get('joining-date')
		salary = request.form.get('salary')

		conn = get_db_connection()
		
		curs = conn.cursor()
		curs.execute("INSERT INTO developers (name, email, joining_date, salary) VALUES (?,?,?,?)", (name, email, joining_date, salary))
		conn.commit()
		
		conn.close()
		
		return redirect(url_for('index'))

	return render_template('index.html')
	
@app.route('/about/')
def about():
	return render_template('about.html')
	
if __name__ == '__main__':
	app.run(debug=True)

