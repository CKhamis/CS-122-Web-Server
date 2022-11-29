# ----------------------------------------------------------------------
# Name:        flaskapp
# Purpose:     Demonstrate web development with Flask
#
# Author:      Constantin Khamis
# ----------------------------------------------------------------------
"""
Module containing a starter web application.

Download and save into your PyCharm project.
Run the program.
Point your browser to http://localhost:5000
"""
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def welcome():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
