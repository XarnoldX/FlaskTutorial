#  forms module stores web form classes

from flask_wtf import FlaskForm  # the forms extension we've installed to venv
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):  # form class defines the fields of the form as class variables
    username = StringField('Username', validators=[DataRequired()])  # object as a class variable
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')