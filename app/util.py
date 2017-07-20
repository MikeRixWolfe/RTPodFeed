#!/usr/bin/env python
from json import loads
from app import app, cache


@cache.memoize(300)
def get_episodes():
    with app.open_resource('persist/episodes', 'r') as f:
        return loads(f.read())
