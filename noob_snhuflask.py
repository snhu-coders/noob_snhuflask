"""
This script is intended to function as a Flask-served
RESTful API to supplement the functions of Noob SNHUbot.

Be warned.  I have no idea what I'm doing.
"""

# Import some stuff here.

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!\n"

if __name__ == "__main__":
    app.run()