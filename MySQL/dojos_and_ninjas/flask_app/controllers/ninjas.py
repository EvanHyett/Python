from flask import render_template, request, redirect
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja
from flask_app import app

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template("create_ninja.html", dojos = dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojos_id' : request.form['dojos_id']
    }
    Ninja.create_ninja(data)
    return redirect('/add_ninja')