from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.all_todo, name='index'),
    #url(r'/test', views.all_todo, name='test')
]
