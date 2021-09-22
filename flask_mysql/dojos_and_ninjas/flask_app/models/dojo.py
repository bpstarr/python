from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo))
        return dojos
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,updated_at) VALUES (%(name)s,NOW());"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return results
    
    @classmethod 
    def show_dojo_and_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(chosen_id)s"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row_from_db in results:
            ninjas_data = {
                "id" :row_from_db["ninjas.id"],
                "first_name":row_from_db["first_name"],
                "last_name":row_from_db["last_name"],
                "age":row_from_db["age"],
                "updated_at":row_from_db["updated_at"],
                "created_at":row_from_db["created_at"]
            }
            dojo.ninjas.append( Ninja(ninjas_data))
        return dojo

