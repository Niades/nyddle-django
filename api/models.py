from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    pub_date = models.DateTimeField()
