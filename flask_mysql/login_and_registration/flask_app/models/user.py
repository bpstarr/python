from flask_app import Flask, app
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

class User():
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_in_login_registration').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(hashed_pw)s);"
        return connectToMySQL('users_in_login_registration').query_db(query,data)
    @staticmethod
    def user_validator(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name']) < 3:
            flash('First name needs to be at least 3 character long.')
            is_valid = False
        if len(data['last_name']) <3:
            flash('Last name needs to be at least 3 character long.')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Email is invalid!')
            is_valid = False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('users_in_login_registration').query_db(query,data)
        if len(results) != 0:
            flash('Email already exists. Please try logging in')
            is_valid = False
        if len(data['password']) < 8:
            flash('Password must be at least 8 characters')
            is_valid = False
        if data['password'] != data['verify_password']:
            flash('Passwords must match')
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('users_in_login_registration').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])