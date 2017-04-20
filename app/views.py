from flask import render_template, send_file
from app import app
from .util import get_episodes


@app.route('/feed', strict_slashes=False, methods=['GET'])
def index():
    # Get a proper loading wheel
    #flash('Loading...', 'success')

    episodes = get_episodes(app.config['PODCASTS_CSV'].split(','))

    return render_template('index.html',
                           eps=episodes)

# Helper for running behind nginx because I'm lazy
@app.route('/feed/images/<image>', strict_slashes=False, methods=['GET'])
def nginx_img_helper(image):
    return send_file('images/' + image, mimetype='image/png')

