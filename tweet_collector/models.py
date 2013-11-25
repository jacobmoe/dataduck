from django.db import models
from tweet_collector.setup.twitter import *
from datetime import *

class Tweet(models.Model):
    message = models.TextField(max_length = 160, db_index = True, null = True)
    latitude = models.FloatField(db_index = True, null = True)
    longitude = models.FloatField(db_index = True, null = True) 
    user_location = models.TextField(max_length = 100, db_index = True, null = True)
    user_language = models.CharField(max_length = 5, db_index = True, null = True)
    tweet_location = models.TextField(max_length = 200, db_index = True, null = True)
    date_tweeted = models.DateTimeField('date tweeted', db_index = True, null = True)

    def __str__(self):
        return self.message

class Collector(object):

    def __init__(self, track):
        self.track = track

    def start(self):

        iterator = twitter_stream.statuses.filter(track = self.track)
        for raw_tweet in iterator:

            print("-----------------------------------------")
            print(raw_tweet)

            if (raw_tweet['coordinates'] is not None):
                print("coordinates TYPE ~~~~~~~~~~> ")
                print(type(raw_tweet['coordinates']))
                print(raw_tweet['coordinates'])
                latitude = raw_tweet['coordinates']['coordinates'][0]
                longitude = raw_tweet['coordinates']['coordinates'][1]
            else:
                latitude = None
                longitude = None

            date = datetime.strptime(
                raw_tweet['created_at'], 
                '%a %b %d %H:%M:%S +0000 %Y'
            )

            tweet = Tweet(
                message = raw_tweet['text'],
                tweet_location = raw_tweet['place'],
                latitude = latitude,
                longitude = longitude,
                user_location = raw_tweet['user']['location'],
                user_language = raw_tweet['user']['lang'],
                date_tweeted = date
            )
            tweet.save()
            print("Saved tweet ==========> %(tweet)s" % locals())