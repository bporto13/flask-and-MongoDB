# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:ZC7CPwrCgI5aqIAe@cluster0.l3upq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    #connect to the db
    collection = mongo.db.events
    #find all data
    events = collection.find({'event':'Homecoming'})
    #return a message
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    events = mongo.db.events
    # insert new data
    events.insert({"event":"Susan's birthday", "date":"2020-07-30"})
    # return a message to the user
    return "Event added"
