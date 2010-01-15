from django.conf.urls.defaults import *

urlpatterns = patterns(
    'madscientist.home.views',

    url(r'^$', 'home'),
)

