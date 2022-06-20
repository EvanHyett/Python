
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas
from flask_app import DATABASE

DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # GET ALL DOJOS
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    # CREATE DOJO
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_id

    
    # SHOW NINJAS IN EACH DOJO
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        for data in results:
            ninja_data = {
                "id" : data["id"],
                "first_name" : data["first_name"],
                "last_name" : data["last_name"],
                "age" : data["age"],
                "created_at" : data["created_at"],
                "updated_at" : data["updated_at"],
                "dojos_id" : data["dojos_id"]
            }
            dojo.ninjas.append(ninjas.Ninja(ninja_data))
        return dojo