from django.shortcuts import render
from datetime import *
from django.utils.timezone import utc

from tweet_collector.models import *

def start(request):
    start_date = datetime.now().replace(tzinfo=utc)
    stop_date = start_date + timedelta(minutes=5)
    track = request.POST.get('track')

    collection_period = CollectionPeriod(
        start_date = start_date,
        stop_date = stop_date,
        search_terms = track
    )
    collection_period.save()
    collector = Collector(collection_period)
    collector.start()
    return render(
        request, 
        'tweet_collector/collect.html',
        {'message': 'Collection completed'}
    )


def stop(request, collection_period_id):
    CollectionPeriod.stop

def collect(request):
    return render(
        request, 
        'tweet_collector/collect.html',
        {}
    )

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

