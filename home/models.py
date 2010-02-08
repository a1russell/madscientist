from django.db import models

class NewsItem(models.Model):
    """\
    News item for the What's New page

    """
    event_date = models.DateField()
    body = models.TextField()

    def __unicode__(self):
        return self.body

