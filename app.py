from flask import Flask, render_template, request
# if i were to install smth, "pip install xxx" in TERMINAL
import joblib

model = joblib.load("DBS_SGD_model.pkl")

app = Flask(__name__) # Flask object

@app.route("/", methods = ["GET","POST"]) # This creates the "brain" of application. Framework is FIXED! "app" is the standard name everyone uses, and __name__ is a special Python variable that helps Flask find our files.
# GET: It shows the user the webpage (eg., a blank login form).
# POST: It receives the data the user typed into that form.


def index():
    return(render_template('index.html'))


@app.route("/main", methods = ["GET","POST"]) 
def main():
    return(render_template('main.html'))

@app.route("/dbs", methods = ["GET","POST"]) 
def dbs():
    return(render_template('dbs.html'))

@app.route("/dbsPrediction", methods = ["GET","POST"]) 
def dbsPrediction():
    q = float(request.form.get("q")) #Information from a website always arrives as "Text." Since my model performs math, you must convert that text into a decimal number (float).
    r = model.predict([[q]]) 
    r = r[0][0]
    return(render_template('dbsPrediction.html', r = r)) # the "r = r" second "r" is front end ("r = r" is connecting the Python calculation to the HTML display.)

"""
>>>> [[q]]
Machine learning models are designed to handle "batches" of data (like a whole spreadsheet). Even if you only have one number, the model expects a 2D structure (rows and columns).
- q is just a number.
- [q] is a list (one row).
- [[q]] is a nested list (a table with one row and one column).
"""


## Each interface will have one whole new HTML file (in this case index.html, main,html & dbs.html), HTML is used to provide the structure and content of a web page. It is the fundamental building block of the web and works by using "markup" to define elements like headings, paragraphs, images, and links for display in a web browser. (front-end interface)

if __name__ == "__main__":
    app.run()


"""
1. Every time we run a Python file, Python creates a hidden variable called "__name__" 
   and attaches it to that file.

2. Python has a very simple rule for what it writes on that badge:
a. If you run the file directly (by typing python app.py): Python thinks, "This is the main script I'm supposed to focus on." So, it writes "__main__" on the badge.
b. If the file is imported (someone else uses import app): Python thinks, "This file is just a helper for another script." So, it writes the actual filename ("app") on the badge.
"""