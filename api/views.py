from django.http import HttpResponse
from django.core import serializers
from .models import NewsItem


def get_news(request):
    if request.method == 'GET':
        news = NewsItem.objects.order_by('-pub_date')[:10]
        return HttpResponse(serializers.serialize('json', news))
    else:
        return HttpResponse(status=405)
