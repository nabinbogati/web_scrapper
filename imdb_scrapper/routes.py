from flask import render_template, url_for, flash, redirect, request
from imdb_scrapper import app
from imdb_scrapper.forms import SearchForm

from imdb_scrapper.config import BASE_URL

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
           return redirect(url_for('index'))
        else:
            flash(f'Invalid Search Query ! Enter Atleast 3 Letters !', 'danger')
            
    return render_template('index.html', title='Search', form=form)

        

