from flask_app.config.mysqlconnection import connectToMySQL
from .favorite_author import Favorite

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    @classmethod
    def create_new_author(cls,data):
        query = "INSERT INTO authors (name,created_at,updated_at) VALUES (%(name)s,NOW(),NOW());"
        results = connectToMySQL('books_schema').query_db(query,data)
        return results
    @classmethod
    def show_authors_favorite_books(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id WHERE author_id = %(chosen_id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        print(results)
        author = cls(results[0])
        for row_from_db in results:
            favorites_data  = {
                "id":row_from_db["favorites.id"],
                "author_id":row_from_db["author_id"]
            }
            author.favorites.append( Favorite(favorites_data))
        return author

        
