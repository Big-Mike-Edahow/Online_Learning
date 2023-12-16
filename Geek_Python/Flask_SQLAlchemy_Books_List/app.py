# app.py
# Flask-SQLAlchemy Booklist

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Big Mike is going to code all weekend'

db = SQLAlchemy()
db_name = 'books.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, unique=True)
    author = db.Column(db.String(500), nullable=False)

def create_db():
    with app.app_context():
        db.create_all()

# Home route
@app.route('/')
def home():
    details = Books.query.all()
    return render_template('home.html', details=details)
 
 
# Add data route
@app.route('/add', methods=['GET', 'POST'])
def add_books():
    if request.method == 'POST':
        book_title = request.form.get('title')
        book_author = request.form.get('author')
 
        add_detail = Books(
            title=book_title,
            author=book_author
        )
        db.session.add(add_detail)
        db.session.commit()
        return redirect(url_for('home'))
 
    return render_template('books.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    create_db()
    app.run(debug=True)

