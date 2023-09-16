from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    year = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"{self.name} - {self.description}"
    
 
@app.route('/')
def index():
    return 'Hello!'


# Create a route that when it is visited,, it displays all the drinks in the database
@app.route('/books')
def get_books():
    books = Book.query.order_by(Book.title).all()
    output = []

    for book in books:
        book_data = {'Id': book.id, 'Title': book.title}
        output.append(book_data)
    return {"books": output}


@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"Id": book.id, "Title": book.title}


@app.route('/books', methods=['POST'])
def add_book():
    book = Book(id=request.json['Id'], title=request.json['Title'])
    db.session.add(book)
    db.session.commit()
    return {'id':book.id}


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "item deleted"}
