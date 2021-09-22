from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.book import Book

@app.route('/books')
def show_all_books():
    books = Book.get_all()
    print(books)
    return render_template('books.html',books = books)
@app.route('/create_new_book', methods = ['POST'])
def create_new_book():
    data = {
        'title' : request.form['title'],
        'num_of_pages':request.form['num_of_pages']
    }
    Book.create_new_book(data)
    return redirect('/books')
@app.route('/books/<id>')
def show_single_book(id):
    data = {
        'chosen_id': id
    }
    this_book = Book.show_single_book(data)
    return render_template('show_book.html', show_book = this_book)

