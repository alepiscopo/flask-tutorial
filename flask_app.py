# flask_app.py
from flask import Flask, jsonify, request
import config
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# Set debug status
if config.ENVIRONMENT == 'development':
    app.config["DEBUG"] = True
else:
    app.config["DEBUG"] = False

# Set db config
for key, value in config.DB[config.ENVIRONMENT].items():
    app.config[key] = value
db = SQLAlchemy(app)
__tablename__ = "big_table"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def hello():
    return "Show me this message and nothing else!"
    #if message:
    #    return message
    #else:
    #    return "There is no message!"

@app.route("/api", methods=["GET", "POST"])
def generate_json():
    if request.method == 'POST':
        data = request.get_json(force=True)
        #print(request.form['person_1'])
        for key in data.keys():
            user_id = key.split('_')[1]
            user_name = data[key]['name']
            user_surname = data[key]['surname']
            user_data = User(id=user_id, name=user_name, surname=user_surname)
            db.session.add(user_data)
        db.session.commit()
        print("data committed!")
        df = pd.DataFrame.from_dict(data, orient="index")
        person_names = df['name'].tolist()
        no_people = len(person_names)
        return f"In my group, there are {no_people} people: {person_names[0]}, {person_names[1]}, {person_names[2]}, and {person_names[3]}"
    else:
        data = {"person_1":{"name":"Alessandro", "surname":"Piscopo"}, "person_2":{"name":"Someone", "surname":"Else"}, "person_3":{"name":"Another", "surname":"One"}, "person_4":{"name":"One", "surname":"More"}}
        return jsonify(data)


    #return jsonify(data)
