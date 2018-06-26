# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    # return HttpResponse('Hello,world!')
    # return render(request,'blog/index.html')
    # return render(request,'blog/index.html',{'param':'Hello Blog'})
    article=models.Article.objects.get(pk=1)
    return render(request,'blog/index.html',{'article':article})


'''失败！！！'''
def list(request):
    articles=models.Article.objects.all()
    return render(request,'blog/list.html',{'articles',articles})