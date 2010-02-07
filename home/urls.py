from django.conf.urls.defaults import *

whats_new_info = {}

urlpatterns = patterns(
    'madscientist.home.views',

    url(r'^$', 'home', name='home'),
)

urlpatterns += patterns(
    'django.views.generic.simple',

    url(r'^faq/$', 'direct_to_template',
        {'template': 'home/faq.html',}, 'faq'),
)

urlpatterns += patterns(
    'django.views.generic.list_detail',

    url(r'^whats_new/$', 'object_list', whats_new_info, 'whats_new'),
)

