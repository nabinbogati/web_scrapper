from imdb_scrapper import db
from datetime import datetime

class Imdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(100), unique=False, nullable=False)
    category = db.Column(db.String(50), unique=False, nullable=False)
    results = db.Column(db.String(1000), unique=False, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Imdb('{self.keyword}', '{self.results}')"
