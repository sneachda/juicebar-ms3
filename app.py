import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

# Config Settings & Environmental Variables located in env.py // connecting to database
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

'''
Home Page
'''

'''
@app.route('/')
def home_page():
    return render_template("home.html")
'''

#Recipes
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.getenv("IP",),
            port=int(os.getenv("PORT",)),
            debug=True)
