from flask_app.config.mysqlconnection import connectToMySQL

class Favorite: 
    def __init__(self,data):
        self.id = data['id']
        self.book_id = data['book_id']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id ;"
        results = connectToMySQL('books_schema').query_db(query)
        print(results)
        return results