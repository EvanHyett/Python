from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create_user' , methods=["POST"])
def create_user():
    User.create(request.form)
    return redirect('/display')


@app.route('/display')
def display_users():
    users = User.get_all()
    return render_template("display.html", users = users)


@app.route('/user/<int:id>/show')
def show_user(id):
    users = User.show_one({'id' : id})
    return render_template("showuser.html", user = users)


@app.route('/user/<int:id>/edit')
def edit(id):
    user = User.show_one({'id' : id})
    return render_template("edit.html", user = user)


@app.route('/edit', methods=["POST"])
def edit_one():
    User.edit_one(request.form)
    return redirect('/display')



@app.route('/user/<int:id>/delete')
def delete_user(id):
    User.delete_one({'id' : id})
    return redirect('/display')


if __name__ == "__main__":
    app.run(debug=True)

