import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from forms import RegistrationForm, LoginForm
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
bcrypt = Bcrypt(app)


'''
Home Page
User can choose to see all recipes
or can browse by category: smoothies or juices.
'''


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


'''
Recipes 
'''


# all recipes display
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', title='All Recipes',
                           recipes=mongo.db.recipes.find())


'''
User 
'''


# Register
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        # If there is no existing user, the entered password is hashed for security before being sent to store in the DB
        if existing_user is None:
            # hashes the entered password
            hashed_password = bcrypt.generate_password_hash(request.form['password'])
            users.insert({'username': request.form['username'], 'password': hashed_password})
            session["username"] = request.form['username']
            flash('Your account has been successfully created.')
            return redirect(url_for('index'))
        flash('That username is taken! Please choose another username.')
    return render_template('register.html', form=form, title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        # Variable for users collection
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user:
            if bcrypt.check_password_hash(existing_user['password'], request.form['password']):
                # Add user to session if passwords match
                session['username'] = request.form['username']
                flash('You have been successfully logged in!')
                return redirect(url_for('index'))
            else:
                # if user entered incorrect password
                flash("Incorrect username or password. Please try again")
                return redirect(url_for('login'))
        elif not existing_user:
            flash("Username does not exist! Please try again")
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))


'''
Error
'''


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)
