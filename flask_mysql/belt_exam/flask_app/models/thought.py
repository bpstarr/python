from flask_app import app
from flask import flash 
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import like
class Thought():
    def __init__(self,data):
        self.id = data['id']
        self.thought = data['thought']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.likes = data['likes']
        self.creator = None
        self.creator2 = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM thoughts;"
        results = connectToMySQL('belt_exam').query_db(query)

        thoughts = []

        for thought in results:
            thoughts.append(cls(thought))
        return thoughts
    
    @classmethod
    def get_all_with_users_and_likes(cls):
        query = "SELECT * FROM thoughts LEFT JOIN users ON thoughts.user_id = users.id LEFT JOIN likes ON thoughts.id = likes.thought_id;"
        results = connectToMySQL('belt_exam').query_db(query)
        list = []

        for object in results:
            data = {
                "id" : object['users.id'],
                "first_name": object['first_name'],
                "last_name": object['last_name'],
                "email":object['email'],
                "password":object['password'],
                "created_at": object["users.created_at"],
                "updated_at": object["users.updated_at"],

            }
        for object2 in results:
            data = {
                "id": object2['likes.id'],
                "likes":object2['likes'],
                "user_id":object2["user_id"],
                "thought_id":object2["thought_id"]

            }
            t = cls(object)
            c = cls(object2)
            t.creator = user.User(data)
            c.creator2 = like.Like(data)
            list.append(t)
            list.append(c)
        return list
    
    @classmethod
    def show_users_thoughts(cls,data):
        query = "SELECT * FROM thoughts WHERE user_id = %(id)s;"
        results = connectToMySQL('belt_exam').query_db(query,data)

        thoughts = []

        for thought in results:
            thoughts.append(cls(thought))
        print(thoughts)
        return thoughts


    @classmethod
    def add_thought(cls,data):
        query = "INSERT INTO thoughts (thought,user_id) VALUES (%(thought)s,%(user_id)s);"
        results = connectToMySQL('belt_exam').query_db(query,data)
        print(results)
        return results

    @classmethod
    def delete_thought(cls, data):
        query = "DELETE FROM thoughts WHERE id = %(id)s"
        results = connectToMySQL('belt_exam').query_db(query,data)
        print(results)
        return results
    
    @classmethod
    def like(cls,data):
        query = "UPDATE thoughts SET likes = like+1 WHERE id = %(id)s"
        results = connectToMySQL('belt_exam').query_db(query,data)
        return results
    
    @classmethod
    def unlike(cls,data):
        query = "UPDATE thoughts SET likes = like-1 WHERE id = %(id)s"
        results = connectToMySQL('belt_exam').query_db(query,data)
        return results
    
    @staticmethod
    def thought_validator(thought):
        is_valid = True
        if len(thought['thought']) < 5:
            flash("thought must be at least 5 characters long")
            is_valid = False
        if len(thought['thought']) == 0:
            flash("Thought cannot be empty")
            is_valid = False
        return is_valid
