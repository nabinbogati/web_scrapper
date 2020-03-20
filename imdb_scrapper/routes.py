from flask import render_template, url_for, flash, redirect, request
from flask_paginate import Pagination, get_page_args
from imdb_scrapper import app, db
from imdb_scrapper.forms import SearchForm
from imdb_scrapper.crawler import crawl
from imdb_scrapper.models import Imdb

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            key_word = form.search.data.replace(' ', '').lower()
            cat = form.categories.data
            db_result = Imdb.query.filter_by(keyword=key_word, category=cat).all()
            if db_result:
                print("From Database")
                flash(f'!! Showing From Database !!', 'success text-center')
                return render_template('index.html', title='Search', form=form, data=db_result)
            else:
                results = crawl(query=form.search.data, query_type=form.categories.data)
            
                if results is not None:
                    data = results
                    for result in results:
                        result = Imdb(keyword=key_word, category=cat, results=result)
                        db.session.add(result)
                    db.session.commit()
                    print("Database Updated")

                    flash(f'!! Showing From Website !!', 'success text-center')
                    return render_template('index.html', title='Search', form=form, data=data)
                else: 
                    flash(f'!! No Results Found !!', 'danger text-center ')
                    return redirect(url_for('index'))
        else:
            flash(f'Invalid Search Query ! Enter at least 3 letters and at most 100 letters !', 'danger text-center ')
            return redirect(url_for('index'))
    return render_template('index.html', title='Search', form=form)

        

