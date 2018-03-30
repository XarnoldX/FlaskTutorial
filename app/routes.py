from flask import render_template
from app import app
from app.forms import LoginForm  # import the LoginForm class from forms.py

@app.route('/')  # home page
@app.route('/index')
def index():
    user = {'username': 'Arnold'}  # user object until we have a db
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
    return render_template('index.html', title='Home', user=user, posts=posts)  # render the index template and insert variables

@app.route('/login', methods=['GET', 'POST'])  # login form, accepts GET and POST requests (GET is default)
def login():
    form = LoginForm()  # instantiate an object from LoginForm class
    if form.validate_on_submit():  # form processing - gather all the data, run all the validators
        flash('Login requested for user {}, remember_me={}'.format(  # show a message to the user - action success, failure... - they need to be rendered in templates
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))  # redirect to page
    return render_template('login.html', title='Sign In', form=form)  # send the object to the template