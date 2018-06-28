# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse

''''
json字符串  在python中 json是字符串 调用接口返回的是json字符串；接口提供方提供的也是json字符串
return之前需要将dict转为json字符串  json.dumps(dict_data)
调用接口 获取返回值之后 需要立刻将json字符串转为dict类型数据。 json.loads(json_data) 这样才能获取其中需要的字段
'''
def index(request):
    dict_data = {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'str': 'abc'}
    json_dupms = json.dumps(dict_data)
    json_loads = json.loads(json_dupms)

    print('dict_data : {}'.format(dict_data))
    print('json_dupms : {}'.format(json_dupms))
    print('json_loads : {}'.format(json_loads))

    result = str(dict_data)
    print('result type : {}'.format(type(result)))
    print('result : {}'.format(result))

    return HttpResponse(result)