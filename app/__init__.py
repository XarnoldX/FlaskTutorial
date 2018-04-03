from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  # db object represents the database
migrate = Migrate(app, db)  # object represents the migration engine
login = LoginManager(app)  # login extension is initialized
login.login_view = 'login'  # view function that handles login - name used in a url_for() call to get the URL

from app import routes, models  # import models module, this will define the structure of the database