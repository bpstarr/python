from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/authors')
def get_index():
    authors = Author.get_all()
    print(authors)
    return render_template('index.html', authors = authors)
@app.route('/create_new_author', methods = ['POST'])
def create_new_author():
    data = {
        'name': request.form['name']
    }
    Author.create_new_author(data)
    return redirect('/authors')
@app.route('/authors/<author_id>')
def show_authors_favorite_books(author_id):
    data = {
        "chosen_id"  : author_id  
    }
    this_author = Author.show_authors_favorite_books(data)
    # favorite_books = Book.show_authors_favorite_books(data)
    return render_template('show_author.html',specific_author = this_author)#favorite_books = favorite_books)

