# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# Create your views here.
from mysql_demo.model.mysql_connector_python_base import select_mysql2 as select02
from mysql_demo.model.mysql_connector_python_base import select_mysql3 as select03
from mysql_demo.model.mysql_connector_python_base import selectByUsername as select04
from mysql_demo.model.mysql_python_base import select_mysql as select05

import json

def index(request):
    values=select02()
    print('type of valus : {}, value : {}'.format(type(values),values))
    jsonData=json.dumps(values[0],encoding='utf-8',ensure_ascii=False)
    return HttpResponse(jsonData)
    # return HttpResponse('ok')


def index3(request):
    values=select03()
    jsonData=json.dumps(values[0],encoding='utf-8',ensure_ascii=False)
    print('type of valus : {}, value : {}, jsonData : {}'.format(type(values), values,jsonData))
    return HttpResponse(jsonData)
    # return HttpResponse('ok')

'''
http://localhost:8000/mysql/index4/?username=上海公司
'''
def index4(request):
    if request.method == 'POST':
        return HttpResponse('please use get method')
    elif request.method == 'GET':
        username = request.GET.get('username')
    if username.strip() == '':
        return HttpResponse('request username param is null')
    print('username : {}'.format(username))
    values=select04(username)
    jsonData=json.dumps(values,encoding='utf-8',ensure_ascii=False)
    print('type of valus : {}, value : {}, jsonData : {}'.format(type(values), values, jsonData))
    return HttpResponse(jsonData)

'''
http://localhost:8000/mysql/index5/?username=上海公司
'''
def index5(request):
    username = request.GET.get('username')
    if username.strip() == '':
        return HttpResponse('request username param is null')
    print('username : {}'.format(username))
    values=select05(username)
    jsonData=json.dumps(values,encoding='utf-8',ensure_ascii=False)
    print('type of valus : {}, value : {}, jsonData : {}'.format(type(values), values, jsonData))
    return HttpResponse(jsonData)


def json_test():
    dict_data = ['123','上海','asb']
    json_data=json.dumps(dict_data,encoding='utf-8',ensure_ascii=False)
    print(json_data)


if __name__ == '__main__':
    json_test()