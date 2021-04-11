from flask import Flask, render_template
from flask.globals import request
import pandas as pd
from ast import literal_eval


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search/', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']

        with open("static/ex.csv", "r") as csvf:
            data = pd.read_csv(
                "static/ex.csv", 
                )

            nammes = list(data.name)
            urls = list(data.url)
            pswrds = list(data.password)
            usrnmes = list(data.username)

            try:
                _index = nammes.index(str(name))
                json = {
                    "url": "{}".format(urls[_index]),
                    "name": "{}".format(nammes[_index]),
                    "username": "{}".format(usrnmes[_index]),
                    "password": "{}".format(pswrds[_index])
                }
                return render_template("index.html", dta = json, info = True)
            except ValueError:
                return "None"

if __name__ == '__main__':
    app.run(debug=True)