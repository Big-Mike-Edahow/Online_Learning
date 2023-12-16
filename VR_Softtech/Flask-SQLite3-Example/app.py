# app.py
# Flask-SQLite3 Contacts List

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Big Mike is in Sweet Home Alabama'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/index')
def index():
    conn = get_db_connection()
    curs=conn.cursor()
    sql_version = curs.execute("SELECT sqlite_version();").fetchall()
    data = curs.execute("SELECT * FROM users;").fetchall()
    user_ip = request.remote_addr.format()
    conn.commit()
    conn.close()

    return render_template('index.html', sql_version=sql_version, data=data, user_ip=user_ip)

@app.route('/add_user', methods = ['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user_name = request.form.get('user-name')
        contact = request.form.get('contact')

        conn = get_db_connection()
        curs=conn.cursor()

        curs.execute("INSERT INTO users (user_name, contact) values (?,?)",(user_name, contact))

        conn.commit()
        conn.close()

        flash('User Added Successfully','success')

        return redirect(url_for('results'))
    
    return render_template('add_user.html')

@app.route('/user_data')
def user_data():
    user_name=request.args.get('user_name')

    conn = get_db_connection()
    curs = conn.cursor()

    curs.execute("select * FROM users where user_name=?",(user_name,))
    data=curs.fetchone()

    return render_template('edit_user.html', data=data)

@app.route('/edit_user', methods = ['GET', 'POST'])
def edit_user():
    if request.method == 'POST':
        user_name = request.form.get('user-name')
        contact = request.form.get('contact')

        conn = get_db_connection()
        curs=conn.cursor()

        curs.execute("UPDATE USERS SET user_name = ?, contact = ? WHERE user_name = ?", (user_name,contact,user_name))

        conn.commit()
        conn.close()

        flash('User Information Updated','success')

        return redirect(url_for('results'))
    
    return render_template('index.html')

@app.route('/delete_user/<string:user_id>', methods = ['GET'])
def delete_user(user_id):
    conn = get_db_connection()
    curs=conn.cursor()

    curs.execute("DELETE FROM users WHERE user_id = ?", (user_id,))

    conn.commit()
    conn.close()

    flash('User Information Deleted','warning')

    return redirect(url_for('results'))
    
@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
    
if __name__=='__main__':
    app.run(debug=True)

