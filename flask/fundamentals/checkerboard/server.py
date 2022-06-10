from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #should display 8 by 8 board
def first():
    return render_template("index.html", x = 8, y = 8, even = "red", odd = "blue")

@app.route('/<int:y>') #should display 8 by 4 board
def second(y):
    return render_template("index.html", x = 8, y = y, even = "red", odd = "blue")

@app.route('/<int:x>/<int:y>') #should display an x by y board
def third(x, y):
    return render_template("index.html", x = x, y = y, even = "red", odd = "blue")

@app.route('/<int:x>/<int:y>/<string:even>/<string:odd>')
def fourth(x, y, even, odd):
    return render_template("index.html", x = x, y = y, even = even, odd = odd)


if __name__ == "__main__":
    app.run(debug = True)