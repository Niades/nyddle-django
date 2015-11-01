from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.post_login),
    url(r'^news', views.get_news),
]
