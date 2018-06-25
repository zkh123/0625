# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('Hello,world!')
    # return render(request,'blog/index.html')
    return render(request,'blog/index.html',{'param':'Hello Blog'})