from django.urls import path
from . import views

urlpatterns = [
    path('', views.crawl_and_show_news, name='crawl_and_show_news'),
]