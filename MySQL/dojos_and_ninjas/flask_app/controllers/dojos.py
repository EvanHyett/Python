from flask import render_template, request, redirect
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja
from flask_app import app

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')

@app.route('/dojos/ninjas/<int:id>')
def get_dojo_with_ninjas(id):
    dojos = Dojo.get_dojo_with_ninjas({'id' : id})
    return render_template("dojos_ninjas.html", dojos = dojos)
