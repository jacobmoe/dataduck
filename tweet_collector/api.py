from tastypie.resources import ModelResource
# from tastypie.contants import ALL
from tweet_collector.models import Tweet

class TweetResource(ModelResource):
    class Meta:
        queryset = Tweet.objects.all()
        resource_name = 'tweet'