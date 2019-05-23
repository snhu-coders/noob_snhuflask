"""
This script is intended to function as a Flask-served
RESTful API to supplement the functions of Noob SNHUbot.

Be warned.  I have no idea what I'm doing.
"""

### Import some stuff here.

import sys
import yaml
import slack
from flask import Flask, jsonify
from slackeventsapi import SlackEventAdapter

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

### Globals

app = Flask(__name__)
slack_client = slack.WebClient(FLASK_CONFIG["token"])
slack_events_adapter = SlackEventAdapter(FLASK_CONFIG["sign-secret"], "/slack/events")

### Function Definitions

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    print(message)

# Print out errors if they occur
@slack_events_adapter.on("error")
def show_error(err):
    print("ERROR: " + str(err))

if __name__ == "__main__":
    slack_events_adapter.start(port=3000)