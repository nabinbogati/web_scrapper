from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired(), Length(min=3, max=50)])
    categories = SelectField('ChooseCategory', validators=[DataRequired()], choices=[('all', 'All'), ('tt', 'Titles'), ('ep', 'Tv Episodes'), ('co', 'Companies'), ('kw', 'Keywords')])
    submit = SubmitField('SEARCH')
