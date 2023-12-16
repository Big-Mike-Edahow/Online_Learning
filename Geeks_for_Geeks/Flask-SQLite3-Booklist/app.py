# app.py
# Flask-SQLite3 Booklist App

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    show_all = conn.execute("SELECT * FROM booklist;").fetchall()
    conn.commit()
    conn.close()

    return render_template('index.html', show_all=show_all)

@app.route('/new_book')
def new_book():
    return render_template('new-book.html')

@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
	if request.method == 'POST':
		book_name = request.form.get('book-name')
		author = request.form.get('author')
		genre = request.form.get('genre')

		conn = get_db_connection()
		curs = conn.cursor()
		curs.execute("INSERT INTO booklist (bookname, author, genre) VALUES (?,?,?)", (book_name, author, genre))
		conn.commit()
		conn.close()
		return render_template("index.html")

	return render_template('index.html')
	
@app.route('/about/')
def about():
	return render_template('about.html')
	
if __name__ == '__main__':
	app.run(debug=True)

