from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Email: 
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_schema').query_db(query)
        email_addresses = []
        for email in results:
            email_addresses.append(cls(email))
        print(email_addresses)
        return email_addresses
    @classmethod
    def create_email(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        results = connectToMySQL('email_schema').query_db(query,data)
        return results
    @staticmethod
    def validate_email(email):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(email['email']):
            flash('Invalid email address!')
            is_valid= False
        return is_valid
        