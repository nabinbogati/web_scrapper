from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from imdb_scrapper.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from imdb_scrapper import routes

