#!/usr/bin/env python
import pytz
import datetime
import os
from random import randint
from flask import Flask
from twython import Twython

app = Flask(__name__)
CONSUMER_KEY=os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET=os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET')

@app.route('/', methods=['POST'])
def tweet():
    # Generate the message that the bot will tweet
    tz = pytz.timezone("US/Pacific")
    msg = "BANG BANG occurred at " + str(datetime.datetime.now(tz))

    # Tweet the message out
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    result = twitter.update_status(status=msg)
    return result

if __name__ == '__main__':
    app.run()
