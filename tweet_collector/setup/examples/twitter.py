from twitter import *

twitter_stream = TwitterStream(
    auth=OAuth(
        OAUTH_TOKEN, 
        OAUTH_SECRET,
        CONSUMER_KEY, 
        CONSUMER_SECRET
    )
)