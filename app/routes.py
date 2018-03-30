from flask import render_template
from app import app

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