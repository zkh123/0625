#-*-coding:utf-8-*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/',views.index),
    url(r'list/',views.list),
]