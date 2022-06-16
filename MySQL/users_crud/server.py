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



if __name__ == "__main__":
    app.run(debug=True)

