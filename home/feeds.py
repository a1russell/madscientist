from django.contrib.syndication.feeds import Feed

from madscientist.home.models import NewsItem


class NewsFeed(Feed):
    title = "What's New"
    link = "/whats_new/"
    description = "Glad you asked."

    def items(self):
        return NewsItem.objects.order_by('-event_date')

    def item_link(self, item):
        return "%s#news_item_%d" % (self.link, item.id,)

