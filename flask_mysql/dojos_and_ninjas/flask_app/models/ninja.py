from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod 
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id,first_name,last_name,age,updated_at) VALUES (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s,NOW());"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return results