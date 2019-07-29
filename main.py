#!/usr/bin/env python
import pytz
import datetime
import os
from random import randint
from flask import Flask, abort, request
from twython import Twython

app = Flask(__name__)
CONSUMER_KEY=os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET=os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET')
POST_KEY = os.environ.get('POST_KEY')

@app.route('/', methods=['POST'])
def tweet():
    data = request.get_json()
    if data and data.get('key') == POST_KEY:
        # Generate the message that the bot will tweet
        tz = pytz.timezone("US/Pacific")
        msg = "BANG BANG occurred at " + datetime.datetime.now(tz).strftime("%m/%d/%Y, %H:%M:%S")

        # Tweet the message out
        twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        result = twitter.update_status(status=msg)
        return result
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
