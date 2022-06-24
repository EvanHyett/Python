from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app import app
from flask_app.models.recipes import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DATABASE = 'recipes'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    @classmethod
    def get_one_with_recipes(cls, data):
        query = "SELECT * FROM users JOIN recipes ON recipes.users_id = users.id WHERE users.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = User(results[0])
        for row_in_db in results:
            recipes_data = {
                "id": row_in_db["recipes.id"],
                "name": row_in_db["name"],
                "description": row_in_db["description"],
                "date": row_in_db["date"],
                "updated_at": row_in_db["recipes.updated_at"],
                "user_id": row_in_db["user_id"],
                "under_thirty": row_in_db["under_thirty"],
                "created_at": row_in_db["recipes.created_at"],
            }
            user.recipes.append(Recipe(recipes_data))
        return user

    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return User(results[0])
        return []


    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if user['confirm_password'] != user['password']:
            is_valid = False
            flash("Passwords must match")
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
