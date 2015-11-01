from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from django.utils.html import strip_tags, escape
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from .models import NewsItem


def get_news(request):
    if request.method == 'GET':
        news = NewsItem.objects.order_by('-pub_date')[:10]
        return HttpResponse(
            serializers.serialize('json', news),
            content_type='application/json'
        )
    else:
        return HttpResponse(status=405)


def post_news(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            json_data = json.loads(request.body)
            new = NewsItem()
            new.title = escape(strip_tags(json_data['title']))
            new.body = escape(strip_tags(json_data['body']))
            new.pub_date = timezone.now()
            new.save()
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def post_login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        user = authenticate(
            username=json_data['username'],
            password=json_data['password']
        )
        if user is not None:
            login(request, user)
            return HttpResponse()
        else:
            # Authentication failed - Forbidden
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=405)
