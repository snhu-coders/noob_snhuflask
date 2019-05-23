"""
This script is intended to function as a Flask-served
RESTful API to supplement the functions of Noob SNHUbot.

Be warned.  I have no idea what I'm doing.
"""

# Import some stuff here.


import sys
import yaml
from flask import Flask, jsonify

# First things first, load the config:

try:
    with open("config.yml", 'r') as file:
        print("Attempting to load config.yml")
        CONFIG = yaml.load(file.read(), Loader=yaml.BaseLoader)
        FLASK_CONFIG = CONFIG["slackflask"]
        """
        Values available via:

        FLASK_CONFIG["token"] for the usual bot token
        FLASK_CONFIG["oauth"] for the oauth token
        FLASK_CONFIG["sign-secret"] for the Slack signing secret
        """
except FileNotFoundError as err:
    print("Could not load config file.  Exiting.")
    sys.exit()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!\n"

if __name__ == "__main__":
    app.run()