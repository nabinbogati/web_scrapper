from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "9832891c9d2fd0cb5885ee7cf4510558"

from imdb_scrapper import routes

