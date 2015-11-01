from django.http import HttpResponse


def get_news(request):
    if request.method == 'GET':
        return HttpResponse('It works')
    else:
        return HttpResponse(status=405)
