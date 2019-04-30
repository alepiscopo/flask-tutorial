# flask_app.py
from flask import Flask, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Show me this message and nothing else!"
    #if message:
    #    return message
    #else:
    #    return "There is no message!"

@app.route("/api")
def generate_json():
    data = {"person_1":{"name":"Alessandro", "surname":"Piscopo"}}
    return jsonify(data)
