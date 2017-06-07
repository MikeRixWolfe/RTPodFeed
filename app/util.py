import datetime
import requests
import xmltodict
from collections import OrderedDict
from dateutil import parser
from app import cache


@cache.memoize(600)
def get_episodes(podcasts):
    episodes = []

    for podcast in podcasts:
        r = requests.get(podcast)
        d = xmltodict.parse(r.text)
        if isinstance(d['rss']['channel']['item'], list):
            episodes += d['rss']['channel']['item']
        else:  # New show, single ep
            episodes.append(d['rss']['channel']['item'])

    episodes = sorted(episodes, key=lambda k: parser.parse(k['pubDate']), reverse=True)

    for i, ep in enumerate(episodes):
        episodes[i] = {
            'author': ep['itunes:author'],
            'date': parser.parse(ep['pubDate']).strftime('%-m/%-d/%Y'),
            'title': ep['title'],
            'time': ep['itunes:duration'],
            'desc': ep['description'],
            'link': ep['link']
        }

    return episodes

