from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^tweets/', include('tweet_collector.urls')),
    (r'^users/', include('users.urls')),
    url(r'^emberduck/$', 'emberduck.views.index'),



)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()