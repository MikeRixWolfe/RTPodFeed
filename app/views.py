from flask import render_template, request
from flask_paginate import Pagination
from app import app
from .util import get_episodes, get_timestamp


@app.route('/feed', strict_slashes=False, methods=['GET'])
def index():
    eps = get_episodes()
    timestamp = get_timestamp()
    per_page = app.config.get('PER_PAGE', 10)

    page = request.args.get('page', type=int, default=1)
    pagination = Pagination(page = page,
                            per_page = per_page,
                            total = len(eps),
                            css_framework = 'foundation',
                            prev_label = '< Prev',
                            next_label = 'Next >')
    page_eps = eps[(page-1)*per_page:page*per_page]

    return render_template('index.html',
                           eps = page_eps,
                           pagination = pagination,
                           timestamp = timestamp)

