from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash




class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.under_thirty = data['under_thirty']

    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date, user_id, under_thirty) VALUES(%(name)s, %(description)s, %(instructions)s, %(date)s, %(user_id)s, %(under_thirty)s)"
        recipe_id = connectToMySQL(DATABASE).query_db(query, data)
        return recipe_id


    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE user_id = %(user_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])


    @classmethod
    def get_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def view_instuctions(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results


    @staticmethod
    def validate_recipe(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            flash("Recipe name must be at least 3 characters.")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 2 characters.")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        if (data['date']) == '':
            flash("Date must be entered")
            is_valid = False
        return is_valid