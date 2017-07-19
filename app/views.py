from flask import render_template, request, send_file
from flask_paginate import Pagination
from json import loads
from app import app, cache


@app.route('/feed', strict_slashes=False, methods=['GET'])
def index():
    with app.open_resource('persist/episodes', 'r') as f:
        eps = loads(f.read())
    per_page = app.config.get('PER_PAGE', 10)

    page = request.args.get('page', type=int, default=1)
    pagination = Pagination(page=page,
                            per_page = per_page,
                            total=len(eps),
                            css_framework='foundation',
                            prev_label='< Prev',
                            next_label='Next >')
    page_eps = eps[(page-1)*per_page:page*per_page]

    return render_template('index.html',
                           eps=page_eps,
                           pagination=pagination)


@app.route('/feed/images/<image>', strict_slashes=False, methods=['GET'])
def send_img(image):
    return send_file('images/' + image, mimetype='image/png')

