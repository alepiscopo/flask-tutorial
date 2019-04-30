# flask_app.py
from flask import Flask, jsonify
import pandas as pd
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
    data = {"person_1":{"name":"Alessandro", "surname":"Piscopo"}, "person_2":{"name":"Someone", "surname":"Else"}, "person_3":{"name":"Another", "surname":"One"}, "person_4":{"name":"One", "surname":"More"}}
    df = pd.DataFrame.from_dict(data, orient="index")
    return df.to_json(orient="index")
    #return jsonify(data)
