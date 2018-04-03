#  forms module stores web form classes
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from flask_wtf import FlaskForm  # the forms extension we've installed to venv
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):  # form class defines the fields of the form as class variables
    username = StringField('Username', validators=[DataRequired()])  # object as a class variable
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')  # submit form

class RegistrationForm(FlaskForm):  # registration form
    username = StringField('Username', validators=[DataRequired()])  # fields with validators
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])  # repeat passport
    submit = SubmitField('Register')

# custom validators in addition to stock validators

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  # check if username already exist
        if user is not None:  # if user exists
            raise ValidationError('Please use a different username.')  # validation error

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()  # check if email already exists
        if user is not None:  # if email exists
            raise ValidationError('Please use a different email address.')  # validation error