#-*-coding:utf-8-*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/',views.index),
    url(r'index3/',views.index3),
    url(r'index4/',views.index4),
    url(r'index5/',views.index5),

]