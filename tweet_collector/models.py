from django.db import models
from tweet_collector.setup.twitter import *

class Tweet(models.Model):
    message = models.CharField(max_length=140)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    time = models.DateTimeField('date tweeted')

    def __str__(self):
        return self.message