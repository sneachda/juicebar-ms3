from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Optional


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=3, max=30)])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Login')


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name',
                              validators=[DataRequired()])
    category_name = IntegerField('Category',
                                 validators=[DataRequired()])
    recipe_description = TextAreaField('Recipe Description',
                                       validators=[DataRequired()])
    prep_time = IntegerField('Cooking Time (minutes)',
                             validators=[DataRequired()])
    it_serves = IntegerField('Number of Servings',
                             validators=[DataRequired()])
    recipe_image = StringField('Recipe Image URL',
                               validators=[Optional()])
    recipe_ingredients = TextAreaField('Ingredients',
                                       validators=[DataRequired()])
    recipe_method = TextAreaField('Directions',
                                  validators=[DataRequired()])
    submit = SubmitField('Add Recipe')
