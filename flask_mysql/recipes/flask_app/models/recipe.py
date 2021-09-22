from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import Flask,app
from flask import flash


class Recipe():

    db_name = 'recipes'
    
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.made_in_under_30mins = data['made_in_under_30mins']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes').query_db(query)

        recipes = []

        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def add_recipe(cls,data):
        query = "INSERT INTO recipes (user_id,name,description,made_in_under_30mins,instructions,date_made) VALUES (%(user_id)s,%(name)s,%(description)s,%(made_in_under_30mins)s,%(instructions)s,%(date_made)s);"
        return connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def show_single_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        thisRecipe = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( thisRecipe[0] )

    @classmethod 
    def edit_recipe(cls,data):
        query = "UPDATE recipes SET name = %(name)s,description = %(description)s,instructions = %(instructions)s,made_in_under_30mins = %(made_in_under_30mins)s,date_made = %(date_made)s Where id = %(id)s"
        connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL('recipes').query_db(query,data)
    
    @staticmethod
    def recipe_validator(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("name must be at least 3 characters long")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters long")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 character long")
            is_valid = False
        if recipe['date_made'] == "":
            is_valid = False
            flash("Please enter a date")
        return is_valid

