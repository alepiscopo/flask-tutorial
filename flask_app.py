# flask_app.py
from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello(*message):
    if message:
        return message
    else:
        return "There is no message!"
