from flask import Flask, render_template, request, flash, redirect 
import cgi, cgitb
import json 
from prediction import get_number_of_days


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction", methods=['GET','POST'])
def prediction():
    future_days = request.form['future_predict']
    if future_days!=None:
        result = get_number_of_days(future_days)
        return render_template('predictions.html', data=result)
    else:
        return render_template('index.html')

@app.route("/table")
def table():
    return render_template('table.html')

@app.route("/table2")
def table2():
    return render_template('table2.html')

if __name__ == "__main__":
    app.run(debug=True)