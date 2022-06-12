
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "counter_evan"


@app.route('/')
def index():
    session['count']+=1
    return render_template("index.html", count = session['count'])


@app.route('/addtwo', methods=['POST'])
def addtwo():
    session['count']+=1
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session['count']=+0
    return redirect('/')



@app.route('/destroy_session')
def destroy():
    session['count']=0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)

