from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo_survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM dojos_surveys_schema;"
        results = connectToMySQL('dojos_survey_schema').query_db(query)
        dojo_survey = []
        for dojo_answers in results:
            dojo_survey.append(cls(dojo_answers))
            return dojo_survey
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos_surveys_schema (name, location,language,comment,created_at,updated_at) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW());"
        results = connectToMySQL('dojos_survey_schema').query_db(query,data)
        return results
    @staticmethod
    def validate_survey_answers(dojos_survey):
        is_valid = True
        if len(dojos_survey['name']) <= 0:
            flash("Name must not be blank.")
            is_valid = False
        if len(dojos_survey['comment']) <= 0:
            flash("comment must be filled out.")
            is_valid = False
        return is_valid



