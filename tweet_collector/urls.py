from django.conf.urls import patterns, include, url
from tweet_collector.api import TweetResource

tweet_resource = TweetResource()

urlpatterns = patterns('',
    url(r'^$', 'tweet_collector.views.index'),
    url(r'^(?P<tweet_id>\d+)/$', 'tweet_collector.views.show'),
    url(r'^collect/$', 'tweet_collector.views.collect'),
    url(r'^start/$', 'tweet_collector.views.start'),
    url(r'^stop/$', 'tweet_collector.views.stop'),
    (r'^api/', include(tweet_resource.urls)),
)