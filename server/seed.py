#!/usr/bin/env python3

from app import db
from models import Book

# Create and add some initial books to the database
if __name__ == '__main__':
    db.create_all()

    book1 = Book(title='Hakuna Matata', author='Mark')
    book2 = Book(title='Ghost of Garbatula', author='Keren')
    book3 = Book(title='CR7 the G.O.A.T', author='Bat-tziyon')

    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)

    db.session.commit()
