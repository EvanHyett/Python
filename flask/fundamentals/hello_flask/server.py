from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html", boxes = 3, color = "aqua")


@app.route('/play/<int:x>')
def play(x):
    return render_template("index.html", boxes = x, color = "aqua")


@app.route('/play/<int:x>/<string:color>')
def playagain(x, color):
    return render_template("index.html", boxes = x, color = color)


if __name__=="__main__":
    app.run(debug=True)