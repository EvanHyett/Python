from flask import Flask
app = Flask(__name__)
app.secret_key = "dojos_and_ninjas_evan"

DATABASE = "dojos_and_ninjas_schema"