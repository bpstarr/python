from flask_app.config.mysqlconnection import connectToMySQL

class Favorite: 
    def __init__(self,data):
        self.id = data['id']
        self.author_id = data['author_id']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors LEFT JOIN favorites ON author.id = favorites.author_id;"
        results = connectToMySQL('books_schema').query_db(query)
        favorites = []
        for favorite in results:
            favorites.append(cls(favorite))
        return favorites
