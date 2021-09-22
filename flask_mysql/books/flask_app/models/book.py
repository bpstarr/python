from flask_app.config.mysqlconnection import connectToMySQL
from .favorite_book import Favorite

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    @classmethod
    def create_new_book(cls,data):
        query = "INSERT INTO books (title,num_of_pages,created_at,updated_at) VALUES (%(title)s, %(num_of_pages)s,NOW(),NOW());"
        results = connectToMySQL('books_schema').query_db(query,data)
        return results
    @classmethod 
    def show_single_book(cls,data):
        query = "SELECT * FROM books WHERE id = %(chosen_id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        print(results)
        return cls(results[0])

    @classmethod
    def show_authors_favorite_books(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id WHERE book.id = %(chosen_id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        print(results)
        book = cls(results[0])
        for row_from_db in results:
            favorite_books  = {
                "id":row_from_db["favorites.id"],
                "book_id":row_from_db["book_id"]
            }
            book.favorites.append( Favorite(favorite_books))
        return book
