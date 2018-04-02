from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  # db object represents the database
migrate = Migrate(app, db)  # object represents the migration engine

from app import routes, models  # import models module, this will define the structure of the database