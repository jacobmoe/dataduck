from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^sign-in/$', 'users.views.sign_in'),
    url(r'^sign-up/$', 'users.views.sign_up'),
    url(r'^create/$', 'users.views.create_user'),
    url(r'^authenticate/$', 'users.views.authenticate_user')
)