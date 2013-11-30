from django.shortcuts import render

from tweet_collector.models import *

def hello(request):
    text = "<ul>"
    for tweet in Tweet.objects.all():
        text += "<li>" + str(tweet) + "</li>"

    return HttpResponse(text + "</ul>")
    # "<p style='font-size: 100px'>Hello, world.</p>")

def collect_tweets(request):
    collection_period = CollectionPeriod(
        start_date = start_date,
        stop_date = stop_date,
        search_terms = track
    )

    collection_period.save()

    collector = Collector(track, collection_period)

    collector.start()

def index(request):
    tweet_list = Tweet.objects.all()
    context = {'tweet_list': tweet_list}
    return render(
        request, 
        'tweet_collector/index.html', 
        context
    )

def show(request, tweet_id):
    tweet = Tweet.objects.get(id = tweet_id)
    return render(
        request, 
        'tweet_collector/show.html', 
        {'tweet': tweet}
    )