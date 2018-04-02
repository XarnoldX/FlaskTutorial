import os
basedir = os.path.abspath(os.path.dirname(__file__))

# separate configuration file

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # used for security tokens in forms
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')  # location of the app db or fallback to main directory of the application defined by basedir
    SQLALCHEMY_TRACK_MODIFICATIONS = False  #signal the application every time a change is about to be made in the db (disabled)