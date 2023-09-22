from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

@app.route('/')
def index():
    from models import Book  # Import the Book model here to avoid circular import
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        from models import Book  # Import the Book model here to avoid circular import
        title = request.form.get('title')
        author = request.form.get('author')
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
