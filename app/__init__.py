from flask import Flask
from flask_caching import Cache

app = Flask(__name__, static_folder='images', static_url_path='/feed/images')
app.config.from_pyfile('app.cfg')
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

from app import views
