from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
class Like():
    def __init__(self,data):
        self.id = data['id']
        self.likes = data['likes']
        self.user_id = data['user_id']
        self.thought_id = data['thought_id']