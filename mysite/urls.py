# urls.py
from django.conf.urls import url, include
#from django.conf.urls.defaults import *
from django.contrib import admin

#admin.autodiscover()

urlpatterns = [
    # Notice the expression does not end in $,
    # that happens at the myapp/url.py level
    url(r'^hej/', include('todo.urls')),
]
