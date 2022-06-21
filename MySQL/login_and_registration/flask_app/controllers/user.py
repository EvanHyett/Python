from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create_user', methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    user_id = User.create(data)
    session['user_id'] = user_id
    print(user_id)
    return redirect(f'/welcome/{user_id}')


@app.route('/welcome/<int:id>')
def welcome_user(id):
    users = User.get_one({'id' : id})
    return render_template("welcome.html", user = users)


@app.route('/login', methods=["POST"])
def login():
    data = {
        'email': request.form['email'],
        'password' : request.form['password']
    }
    user = User.get_email(data)
    if not user:
        flash("Invalid email")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password")
        return redirect('/')
    
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    session['email'] = user.email
    return redirect('/login/user')


@app.route('/login/user')
def login_user():
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    return render_template("login.html")
