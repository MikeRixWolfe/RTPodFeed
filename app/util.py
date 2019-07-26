from datetime import datetime
from os import path
from json import loads
from app import app, cache


@cache.cached(timeout=60, key_prefix='episodes')
def get_episodes():
    with app.open_resource('persist/episodes', 'r') as f:
        return loads(f.read())


@cache.cached(timeout=60, key_prefix='timestamp')
def get_timestamp():
    fpath = path.dirname(path.abspath(__file__)) + '/persist/episodes'
    delta = (int(datetime.now().strftime('%s')) - int(path.getmtime(fpath))) // 60

    if delta == 0:
        return "Updated just now"
    elif delta == 1:
        return "Updated a minute ago"
    else:
        return "Updated {} minutes ago".format(delta)


@app.template_filter('lrep')
def lower_and_replace(text):
    return text.replace(' ', '').lower()

