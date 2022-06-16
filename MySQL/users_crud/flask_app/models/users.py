# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the friend table from our database

DATABASE = 'users_schema'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.create_at = data['create_at']
        self.updated_at = data['updated_at']
        self.full_name = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users



    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, create_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id


    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results


    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])


    @classmethod
    def edit_one(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)