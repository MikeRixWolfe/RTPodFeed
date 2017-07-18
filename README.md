## Description
This is an aggregator for RT podcast feeds linking back to the podcasts on the RT site.


![index.html](/docs/images/feed.png)

## Installation
Install python 2.7.x and then run the following

     git clone https://github.com/MikeRixWolfe/rtpodfeed.git
     sudo pip2 install -r rtpodfeed/requirements.txt

## Setup
### App Setup
Rename app.cfg.default to app.cfg and enter desired information and podcast RSS feeds.
### Adding Podcasts
Add the RSS feed URL (found on the podcast pages on the RT site) and add a square-ish image 
with the name matching the title tag in the RSS feed (lowercase, no spaces, png).

## Usage
#### Server
Run `./run` with supervise/wsgi/whatever.
Add `*/5 * * * * python2 /your/path/here/rtpodfeed/util.py` to crontab to get episodes for the app server.
#### Client
Browse to `http://yoursite.tld/feed` for the podcast feed.

## Requirements
* Python 2.7.x
* Flask
* Flask-Cache
* Flask-Paginate
* Logging
* Requests
* XmlToDict

## License
This software is licensed under the **GPL v3** license. The terms are as follows:
     
     RT Pod Feed
     Copyright (C) 2017  Mike Rix Wolfe
     
     This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     
     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.
     
     You should have received a copy of the GNU General Public License
     along with this program.  If not, see <http://www.gnu.org/licenses/>.
