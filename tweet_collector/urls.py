from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'tweet_collector.views.index'),
    url(r'^(?P<tweet_id>\d+)/$', 'tweet_collector.views.show'),

)