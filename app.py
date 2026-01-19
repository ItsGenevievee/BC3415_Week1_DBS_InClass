from flask import Flask, render_template, request

app = Flask(__name__) # Flask object

@app.route("/", methods = ["GET","POST"]) # This creates the "brain" of application. Framework is FIXED! "app" is the standard name everyone uses, and __name__ is a special Python variable that helps Flask find our files.
# GET: It shows the user the webpage (eg., a blank login form).
# POST: It receives the data the user typed into that form.


def index():
    return(render_template('index.html'))

if __name__ == "__main__":
    app.run()

"""
1. Every time we run a Python file, Python creates a hidden variable called "__name__" 
   and attaches it to that file.

2. Python has a very simple rule for what it writes on that badge:
a. If you run the file directly (by typing python app.py): Python thinks, "This is the main script I'm supposed to focus on." So, it writes "__main__" on the badge.
b. If the file is imported (someone else uses import app): Python thinks, "This file is just a helper for another script." So, it writes the actual filename ("app") on the badge.
"""