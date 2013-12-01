Emberduck = Ember.Application.create({
  LOG_TRANSITIONS: true,
  DEBUG: true,
  LOG_VIEW_LOOKUPS: true,
  rootElement: '#MainContent'
});

Emberduck.Router.map(function() {
    this.resource('tweets', function() {
        this.resource('tweet', {path: ':tweet_id'});
    });
    this.resource('results');
    this.resource('blog');
});

Emberduck.TweetsRoute = Ember.Route.extend({
    model: function() {
        return $.getJSON('/tweets/api/tweet/?format=json').then(function(data) {
            return data.objects.map(function(tweet) {
                tweet.message = tweet.message;
                return tweet;
            });
        });
    }
});

Emberduck.TweetRoute = Ember.Route.extend({
    model: function(params) {
        return $.getJSON('/tweets/api/tweet/?format=json').findBy('id', params.tweet_id);
    }
})
Emberduck.TweetController = Ember.ObjectController.extend({
    isEditing: false,

    actions: {
        edit: function() {
            this.set('isEditing', true);
        },
        doneEditing: function() {
            this.set('isEditing', false);
        }
    },
});

