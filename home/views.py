from django.http import HttpResponse
from django.template import Context, loader

from madscientist.home.models import NewsItem


def home(request):
    template = loader.get_template('home/home.html')
    context = Context({})
    return HttpResponse(template.render(context))


def faq(request):
    template = loader.get_template('home/faq.html')
    context = Context({})
    return HttpResponse(template.render(context))


def whats_new(request):
    news_items = NewsItem.objects.order_by('-event_date')
    template = loader.get_template('home/whats_new.html')
    context = Context({
        'object_list': news_items,
    })
    return HttpResponse(template.render(context))
