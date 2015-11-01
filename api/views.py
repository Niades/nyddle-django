from django.http import HttpResponse


def get_news(request):
    if request.method == 'GET':
        return HttpResponse('It works')
    else:
        # 405 Method Not Allowed
        return HttpResponse(status_code=405)
