from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.id} - {self.title}"


@app.route('/')
def index():
    return 'Hello!'

# New route to page that displays all books in db.
@app.route('/books')
def get_books():
    books = Book.query.order_by(Book.title).all()
    output = []

    for book in books:
        book_data = {'Id': book.id, 'Title': book.title}
        output.append(book_data)
        return {"Books": output}
    

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"Id": book.id, "Title": book.title}


@app.route('/books', methods=['POST'])
def add_book():
    book = Book(author=request.json['Author'], title=request.json['Title'])
    db.session.add(book)
    db.session.commit()
    return {'Id':book.id, 'Author':book.author, 'Title':book.title}


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "item deleted"}