import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo
from flask_bcrypt import Bcrypt
from forms import RegistrationForm, LoginForm, RecipeForm
import math
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
@app.route('/get_recipes')
def get_recipes():
    # pagination - learnt through youtube video from Pretty Printed
    # modified from the Shane Muirhead's project
    limit_per_page = 3
    current_page = int(request.args.get('current_page', 1))
    number_of_all_rec = mongo.db.recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)
    recipes = mongo.db.recipes.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1) * limit_per_page).limit(limit_per_page)
    # get total of all the recipes in db
    return render_template("recipes.html", recipes=recipes,
                           title='All Recipes', current_page=current_page,
                           pages=pages, number_of_all_rec=number_of_all_rec)


# all smoothies
@app.route('/get_smoothies')
def get_smoothies():
    limit_per_page = 3
    current_page = int(request.args.get('current_page', 1))
    number_of_all_rec = mongo.db.recipes.count({"category_name": "Smoothie"})
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)
    recipes = mongo.db.recipes.find({"category_name": "Smoothie"}).sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1) * limit_per_page).limit(limit_per_page)
    return render_template("recipes.html", recipes=recipes,
                           title='Smoothies', current_page=current_page,
                           pages=pages, number_of_all_rec=number_of_all_rec)


# all juices
@app.route('/get_juices')
def get_juices():
    limit_per_page = 3
    current_page = int(request.args.get('current_page', 1))
    number_of_all_rec = mongo.db.recipes.count({"category_name": "Juice"})
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)
    recipes = mongo.db.recipes.find({"category_name": "Juice"}).sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1) * limit_per_page).limit(limit_per_page)
    return render_template("recipes.html", recipes=recipes,
                           title='Smoothies', current_page=current_page,
                           pages=pages, number_of_all_rec=number_of_all_rec)


@app.route('/recipe_full_page/<recipe_id>')
def recipe_full_page(recipe_id):
    full_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_full_page.html",
                           full_recipe=full_recipe,
                           title='Recipe Details')


'''
My Account
'''


# My Recipes
@app.route('/my_recipes/')
def my_recipes():
    if 'username' in session:
        return render_template('my_recipes.html', title='My Account',
                               recipes=mongo.db.recipes.find({"author": session["username"]}))


# add recipe
@app.route('/add_recipe')
def add_recipe():
    if 'username' in session:
        user_logged_in = mongo.db.users.find_one({"username": session['username']})
        if user_logged_in:
            # If user in DB, redirected to Create Recipe page
            form = RecipeForm()
            return render_template('add_recipe.html', title='New Recipe', form=form, categories=mongo.db.categories.find())
    else:
        # Render the page for user to be able to log in
        return render_template("login.html")


# insert recipe
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    if request.method == 'POST':
        recipes = mongo.db.recipes
        recipes.insert_one({
            'category_name': request.form.get('category_name'),
            'recipe_name': request.form.get('recipe_name'),
            'recipe_ ingredients': request.form.get("recipe_ingredients"),
            'recipe_method': request.form.get("recipe_method"),
            'recipe_description': request.form.get('recipe_description'),
            'prep_time': request.form.get('prep_time'),
            'it_serves': request.form.get('it_serves'),
            'recipe_image': request.form.get('recipe_image'),
            'author': session['username']
        })
    flash('Your recipe was added!')
    return redirect(url_for('my_recipes'))


'''
User 
'''


# Register
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Variable for users collection
            users = mongo.db.users
            existing_user = users.find_one({'username': request.form['username']})
            # If there is no existing user
            if existing_user is None:
                # creates the account, hashes the entered password, before sending it to DB storage
                hashed_password = bcrypt.generate_password_hash(request.form['password'])
                users.insert({'username': request.form['username'], 'password': hashed_password})
                session["username"] = request.form['username']
                flash('Your account has been successfully created.')
                return redirect(url_for('index'))
            # if user name is already taken
            flash('Username is taken! Please choose another username.')
    return render_template('register.html', form=form, title='Register')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        # Variable for users collection
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        # checking if the existing user is registered
        if existing_user:
            if bcrypt.check_password_hash(existing_user['password'], request.form['password']):
                # Add user to session if passwords match
                session['username'] = request.form['username']
                flash('You have been successfully logged in!')
                return redirect(url_for('index'))
            else:
                # if password incorrect
                flash("Incorrect username or password. Please try again")
                return redirect(url_for('login'))
        elif not existing_user:
            # if no username  in database
            flash("Username does not exist! Please try again")
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Login')


# Logout
@app.route('/logout')
def logout():
    username = session['username']
    if 'username' in session:
        # This removes the current username from the session
        session.pop('username', None)

        flash(
            "You've successfully logged out. " +
            "See you next time, " +
            username + "!")

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

