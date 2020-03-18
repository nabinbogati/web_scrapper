from flask import render_template, url_for, flash, redirect, request
from imdb_scrapper import app
from imdb_scrapper.forms import SearchForm
from imdb_scrapper.crawler import crawl
from flask_paginate import Pagination, get_page_args

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            results = crawl(query=form.search.data, query_type=form.categories.data)
            
            if results is not None:
                data =  results.to_list()
                flash(f'Search Successful !! Welcome To The World Of Information About Entertainment !!', 'success text-center')
                return render_template('index.html', title='Search', form=form, data=data)
            else: 
                flash(f'!! No Results Found For Your Query !!', 'danger text-center ')
                return redirect(url_for('index'))
        else:
            flash(f'Invalid Search Query ! Enter at least 3 letters and at most 100 letters !', 'danger text-center ')
            return redirect(url_for('index'))
    return render_template('index.html', title='Search', form=form)

        

