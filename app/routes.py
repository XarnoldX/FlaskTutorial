from flask import render_template, redirect, flash, url_for, request
from app import app
from app.forms import LoginForm  # import the LoginForm class from forms.py
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm

@app.route('/')  # home page
@app.route('/index')
@login_required  # login required decorator, it will add a query string argument to redirect URL to get to the requested page
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts)  # render the index template and insert user

@app.route('/login', methods=['GET', 'POST'])  # login form, accepts GET and POST requests (GET is default)
def login():
    if current_user.is_authenticated:  #  if already logged in
        return redirect(url_for('index'))  # redirect to home
    form = LoginForm()  # instantiate an object from LoginForm class
    if form.validate_on_submit():  # form processing - gather all the data, run all the validators
        user = User.query.filter_by(username=form.username.data).first()  # find the user in the db
        if user is None or not user.check_password(form.password.data):  # if no user found or the pw is invalid
            flash('Invalid username or password')  # show a message to the user, needs to be rendered in templates
            return redirect(url_for('login'))  # redirect to login again
        login_user(user, remember=form.remember_me.data)  # log in the user
        next_page = request.args.get('next')  # if there is a next page query string argument
        if not next_page or url_parse(next_page).netloc != '':  # if no next page defined
            next_page = url_for('index')  # return to home
        return redirect(next_page)  #redirect to originally requested page before login
    return render_template('login.html', title='Sign In', form=form)  # send the object to the template

@app.route('/logout')  # logout link
def logout():  # logout function
    logout_user()  # log out the user
    return redirect(url_for('index'))  # redirect to page

@app.route('/register', methods=['GET', 'POST'])  # registration form, accepts GET and POST requests (GET is default)
def register():  # register function
    if current_user.is_authenticated:  # if user is logged in
        return redirect(url_for('index'))  # redirect to index
    form = RegistrationForm()
    if form.validate_on_submit():  # form processing
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()  # write to database
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)  # render the template and pass form data