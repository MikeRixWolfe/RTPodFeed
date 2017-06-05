import datetime
import requests
import xmltodict
from collections import OrderedDict
from dateutil import parser


def get_episodes(podcasts):  # Should cache data so I dont have to get it each time
    episodes = []

    for podcast in podcasts:
        r = requests.get(podcast)
        d = xmltodict.parse(r.text)
        if isinstance(d['rss']['channel']['item'], list):
            episodes += d['rss']['channel']['item']
        else:  # New show, single ep
            episodes.append(d['rss']['channel']['item'])

    episodes = sorted(episodes, key=lambda k: parser.parse(k['pubDate']), reverse=True)

    episodes = episodes[:20]  # Add pagination and remove me

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

