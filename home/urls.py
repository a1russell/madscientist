from django.conf.urls.defaults import patterns, url

from madscientist.home.feeds import NewsFeed

feeds = {
    'whats_new': NewsFeed,
}

urlpatterns = patterns(
    'madscientist.home.views',

    url(r'^$', 'home', name='home'),
    url(r'^faq/$', 'faq', name='faq'),
    url(r'^whats_new/$', 'whats_new', name='whats_new'),
)

urlpatterns += patterns(
    '',

    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),
)
