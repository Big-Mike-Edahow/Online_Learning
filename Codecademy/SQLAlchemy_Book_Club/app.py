# app.py
# Codecademy SQLAlchemy Book Club App

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Study, Code, Review, Repeat'

db = SQLAlchemy(app)

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author = db.Column(db.String(50), index = True, unique = False)
    month = db.Column(db.String(20), index = True, unique = False) #the month of the book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of the book suggestion
    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic', cascade = "all, delete, delete-orphan") #relationship of Books and Reviews
    annotations = db.relationship('Annotation', backref='book', lazy='dynamic', cascade = "all, delete, delete-orphan")
    
    def __repr__(self):
        return "{} in: {},{}".format(self.id, self.month, self.year)

# Reader model
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = False)
    email = db.Column(db.String(120), unique = True, index = True)
    reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic', cascade = "all, delete, delete-orphan")
    annotations = db.relationship('Annotation', backref='author', lazy='dynamic', cascade = "all, delete, delete-orphan") 
    
    def __repr__(self):
        return "Reader ID: {}, email: {}".format(self.id, self.email)

# Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    stars = db.Column(db.Integer, unique = False) #a review's rating
    text = db.Column(db.String(200), unique = False) #a review's text
    book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key column
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    
    def __repr__(self):
        return "Review ID: {}, {} stars {}".format(self.id, self.stars, self.book_id)

# Annotation model
class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(200), unique = False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    #get a nice printout for Annotation objects
    def __repr__(self):
        return '<Annotation {}-{}:{} >'.format(self.reviewer_id, self.book_id, self.text)


def create_db():
    with app.app_context():
        db.create_all()


@app.route('/home')
@app.route('/')
def home():
  books = Book.query.all()
  return render_template('home.html', books = books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        month = request.form.get('month')
        year = request.form.get('year')

        add_detail = Book(
            title=title,
            author=author,
            month=month,
            year=year
        )
        db.session.add(add_detail)
        db.session.commit()
        return redirect(url_for('home'))
 
    return render_template('add_book.html')

@app.route('/profile/<int:user_id>')
def profile(user_id):
   reader = Reader.query.filter_by(id = user_id).first_or_404(description = "There is no user with this ID.")
   return render_template('profile.html', reader = reader)

@app.route('/books/<year>')
def books(year):
   books = Book.query.filter_by(year = year)
   return render_template('display_books.html', year = year, books = books)

@app.route('/reviews/<int:review_id>')
def reviews(review_id):
   #your code here
   review = Review.query.filter_by(id = review_id).first_or_404(description = "There is no user with this ID.")
   return render_template('_review.html', review = review)


if __name__ == '__main__':
    create_db()
    app.run(debug=True)

