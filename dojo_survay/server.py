from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="dojosurvey_evan"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():

    session["your_name"] = request.form['your_name']
    session["location"] =  request.form['location']
    session["language"] = request.form['language']
    session["comments"] = request.form['comments']
    
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug = True)