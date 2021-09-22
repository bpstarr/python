from flask_app import app
from flask import flash 
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from .user import User
class Latte():
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.votes = data['votes']
        self.creator = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM lattes;"
        results = connectToMySQL('belt_exam2').query_db(query)

        lattes = []

        for latte in results:
            lattes.append(cls(latte))
        return lattes
    
    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * FROM lattes JOIN users ON lattes.user_id = users.id;"
        results = connectToMySQL('belt_exam2').query_db(query)
        list = []

        for object in results:
            data = {
                "id" : object['users.id'],
                "first_name": object['first_name'],
                "last_name": object['last_name'],
                "email":object['email'],
                "password":object['password'],
                "created_at": object["users.created_at"],
                "updated_at": object["users.updated_at"]
            }
            t = cls(object)
            t.creator = user.User(data)
            list.append(t)
        return list
    
    @classmethod
    def show_users_lattes(cls,data):
        query = "SELECT * FROM lattes WHERE user_id = %(id)s;"
        results = connectToMySQL('belt_exam2').query_db(query,data)

        lattes = []

        for latte in results:
            lattes.append(cls(latte))
        print(lattes)
        return lattes
    @classmethod 
    def show_single_latte(cls,data):
        query = "SELECT * FROM lattes WHERE id = %(id)s"
        results = connectToMySQL('belt_exam2').query_db(query,data)

        latte = cls(results[0])
        print(latte)
        return latte
    @classmethod
    def get_latte_with_user(cls,data):
        query = "SELECT * FROM lattes LEFT JOIN users ON lattes.user_id = users.id WHERE lattes.id = %(id)s;"
        results = connectToMySQL('belt_exam2').query_db(query,data)
        single_user = cls(results[0])
        list = []
        for object in results:
            data =  {
                "id":object['users.id'],
                "first_name":object['first_name'],
                "last_name":object['last_name'],
                'email':object['email'],
                'password':object['password'],
                'created_at':object['users.created_at'],
                "updated_at":object['users.updated_at']
            }
            # single_user.users.append(user.User(data))
            c = cls(object)
            c.creator = user.User(data)
            list.append(c)
        return list[0]
    @classmethod
    def create_latte(cls,data):
        query = "INSERT INTO lattes (name,filling,crust,user_id) VALUES (%(name)s,%(filling)s,%(crust)s,%(user_id)s);"
        return connectToMySQL('belt_exam2').query_db(query,data)

    @classmethod
    def edit_latte(cls,data):
        query = "UPDATE lattes SET name = %(name)s, filling = %(filling)s, crust = %(crust)s WHERE id = %(id)s"
        return connectToMySQL('belt_exam2').query_db(query,data)

    @classmethod 
    def cast_vote(cls,data):
        query = "UPDATE lattes SET votes = votes+1 WHERE id = %(id)s;"
        return connectToMySQL('belt_exam2').query_db(query,data)
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM lattes WHERE id = %(id)s;"
        return connectToMySQL('belt_exam2').query_db(query,data)

    @staticmethod
    def latte_validator(data):
        is_valid = True
        if len(data['name']) == 0:
            flash("Name cannot be empty")
            is_valid = False
        if len(data['filling']) == 0:
            flash("Filling cannot be empty")
            is_valid = False
        if len(data['crust']) == 0:
            flash("crust cannot be empty")
            is_valid = False
        return is_valid
    
