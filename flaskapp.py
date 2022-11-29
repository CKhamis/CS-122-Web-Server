# ----------------------------------------------------------------------
# Name:        flaskapp
# Purpose:     Demonstrate web development with Flask
#
# Author:      Rula Khayrallah
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
def welcome():
    return "Welcome to CS 122!"

def main():
    app.run()

if __name__ == "__main__":
    main()
