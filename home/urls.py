from django.conf.urls.defaults import *

from madscientist.home.feeds import NewsFeed
from madscientist.home.models import NewsItem

feeds = {
    'whats_new': NewsFeed,
}

news_info = {
    'queryset': NewsItem.objects.order_by('-event_date')
}

urlpatterns = patterns(
    'madscientist.home.views',

    url(r'^$', 'home', name='home'),
)

urlpatterns += patterns(
    '',

    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),
)

urlpatterns += patterns(
    'django.views.generic.simple',

    url(r'^faq/$', 'direct_to_template',
        {'template': 'home/faq.html',}, 'faq'),
)

urlpatterns += patterns(
    'django.views.generic.list_detail',

    url(r'^whats_new/$', 'object_list',
        dict(news_info, template_name='home/whats_new.html'),
        'whats_new'),
)

