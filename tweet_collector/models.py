from django.db import models
from tweet_collector.setup.twitter import *
from datetime import *

class CollectionPeriod(models.Model):
    start_date = models.DateTimeField('start date', db_index = True, null = True)
    stop_date = models.DateTimeField('stop date', db_index = True, null = True)
    search_terms = models.TextField(db_index = True, null = True)

class Tweet(models.Model):
    message = models.TextField(db_index = True, null = True)
    latitude = models.FloatField(db_index = True, null = True)
    longitude = models.FloatField(db_index = True, null = True) 
    user_location = models.TextField(db_index = True, null = True)
    user_language = models.CharField(max_length = 5, db_index = True, null = True)
    tweet_location = models.TextField(db_index = True, null = True)
    date_tweeted = models.DateTimeField('date tweeted', db_index = True, null = True)
    collection_period = models.ForeignKey(CollectionPeriod)

    def __str__(self):
        return self.message

class Collector(object):
    
    def __init__(self, track, start_date, stop_date):
        self.track = track
        self.start_date = start_date
        self.stop_date = stop_date

    def start(self):

        collection_period = CollectionPeriod(
            start_date = self.start_date,
            stop_date = self.stop_date,
            search_terms = self.track
        )

        collection_period.save()

        iterator = twitter_stream.statuses.filter(track = self.track)

        for raw_tweet in iterator:
            if (raw_tweet['coordinates'] is not None):
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
                date_tweeted = date,
                collection_period_id = collection_period.id
            )
            tweet.save()
            print("Saved tweet ==========> %(tweet)s" % locals())

