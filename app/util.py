import re
from datetime import datetime
from json import loads
from os import path
from app import app, cache


@cache.cached(timeout=60, key_prefix='episodes')
def get_episodes():
    with app.open_resource('persist/episodes', 'r') as f:
        return loads(f.read())


@cache.cached(timeout=60, key_prefix='timestamp')
def get_timestamp():
    fpath = path.dirname(path.realpath(__file__)) + '/persist/episodes'
    delta = (int(datetime.now().strftime('%s')) - int(path.getmtime(fpath))) // 60

    if delta == 0:
        return "Updated just now"
    elif delta == 1:
        return "Updated a minute ago"
    else:
        return "Updated {} minutes ago".format(delta)


@app.template_filter('lrep')
def lower_and_replace(text):
    return text.replace(' ', '').replace('*','').lower()


@app.template_filter('timestamp')
def make_timestamp(seconds):
    if seconds is not None:
        seconds = int(seconds)
        h = seconds // 3600 % 24
        m = seconds % 3600 // 60
        s = seconds % 3600 % 60
        if h > 0:
            return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
        else:
            return '{:02d}:{:02d}'.format(m, s)

    return '-'


@app.template_filter('unsponsor')
def unsponsor(text):
    if u'Sponsored by' in text:
        text = re.sub(r'Sponsored by.*', '', text, flags=re.S)
    if u'This episode of Off Topic is sponsored by' in text:
        text = re.sub(r'This episode of Off Topic is sponsored by.*', '', text, flags=re.S)
    if u'Want to contribute' in text:
        text =  re.sub(r'Want to contribute.*', '', text, flags=re.S)
    if u'This episode is sponsored by' in text:
        text = re.sub(r'This episode is sponsored by.*', '', text, flags=re.S)
    if u'This week\'s episode is sponsored by' in text:
        text = re.sub(r'This week\'s episode is sponsored by.*', '', text, flags=re.S)
    if u'Download the full audio' in text:
        text = re.sub(r'Download the full audio.*', '', text, flags=re.S)
    if u'Download the audio' in text:
        text = re.sub(r'Download the audio.*', '', text, flags=re.S)
    if u'This episode is brought to you by' in text:
        text = re.sub(r'This episode is brought to you by.*', '', text, flags=re.S)
    if u'This episode originally aired' in text:
        text = re.sub(r'This episode originally aired.*', '', text, flags=re.S)
    if u'This episode was originally aired' in text:
        text = re.sub(r'This episode was originally aired.*', '', text, flags=re.S)
    if u'This episode was recorded' in text:
        text = re.sub(r'This episode was recorded.*', '', text, flags=re.S)
    if u'This episode originally recorded' in text:
        text = re.sub(r'This episode originally recorded.*', '', text, flags=re.S)
    if u'If you want to send your towel cards in' in text:
        text = re.sub(r'If you want to send your towel cards in.*', '', text, flags=re.S)

    return text.strip()

