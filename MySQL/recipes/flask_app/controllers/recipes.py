from flask import render_template, request, redirect, session, flash
from flask_app.models.recipes import Recipe
from flask_app.models.users import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/add/recipe')
def add_recipe():
    return render_template('addrecipe.html')

@app.route('/create/recipe', methods=["POST"])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/add/recipe')
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "date" : request.form['date'],
        "under_thirty" : request.form['under_thirty'],
        "user_id" : session['user_id']
    }
    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/recipe/instructions/<int:id>')
def view_instructions(id):
    recipe = Recipe.view_instuctions({'id' : id})
    return render_template('view_instructions.html', recipe = recipe)


@app.route('/recipe/<int:recipe_id>')
def single_recipe(recipe_id):
    data = {
        'id' : recipe_id
    }
    recipe = Recipe.view_instuctions(data)
    return render_template("edit_recipe.html", recipe = recipe)

@app.route('/edit/recipe', methods=["POST"])
def edit_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipe/{request.form['recipe_id']}")
    data = {
        "id" : request.form['recipe_id'],
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "date" : request.form['date'],
        "under_thirty" : request.form['under_thirty'],
        "user_id" : session['user_id']
    }
    Recipe.edit_recipe(data)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete_recipe(id):
    Recipe.delete_recipe({'id' : id})
    return redirect('/dashboard')