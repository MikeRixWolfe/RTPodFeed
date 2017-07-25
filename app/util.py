from datetime import datetime
from os import path
from time import daylight, tzname
from json import loads
from app import app, cache


@cache.memoize(120)
def get_episodes():
    with app.open_resource('persist/episodes', 'r') as f:
        return loads(f.read())

@cache.memoize(120)
def get_timestamp():
    fpath = path.dirname(path.abspath(__file__)) + '/persist/episodes'
    timestamp = datetime.fromtimestamp(path.getmtime(fpath)).strftime('%-I:%M %p')

    return "Last updated at {} {}".format(timestamp, tzname[daylight])

