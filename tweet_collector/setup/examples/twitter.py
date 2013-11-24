from twitter import *

twitter = Twitter(
    auth=OAuth(
        OAUTH_TOKEN, 
        OAUTH_SECRET,
        CONSUMER_KEY, 
        CONSUMER_SECRET
    )
)