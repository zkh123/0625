# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

def print_test():
    try:
        result = 1/0
    except ZeroDivisionError:
        print("捕获到除数为零的错误")

def exception_test():
    try:
        result = 4 / 0
    except ZeroDivisionError as reason:
        print(str(reason))
    else:
        print("没有发生异常，输出结果：%d" % result)
    finally:
        print("无论是否发生异常都会执行～")

'''
dataDict=json.loads(data)
print dataDict['Messages'][0]['Body']
'''
def data_type():
    int_data = 1
    float_data = -0.91
    str_data = 'abc'
    flag_data = False
    none_data = None
    PI = 3.14159265359
    list_data = ['Michael', 'Bob', 'Tracy',123]
    tuple_data = ('Michael', 'Bob', 'Tracy',123)
    dict_data = {'Michael': 95, 'Bob': 75, 'Tracy': 85,'str': 'abc'}

    print(dict_data['str'])

    set_data = set([1, 2, 3,'abc'])
    json_data = {"key":"key_data","value":"value_data"}
    print("json_data : {}".format(json_data))

    json_01 = json.dumps(json_data)
    print("json_01 : {}".format(json_01))

    json_02 = json.loads(json_01)
    print("json_02 : {}".format(json_02))

    print('int_data type : {}'.format(type(int_data)))
    print('float_data type : {}'.format(type(float_data)))
    print('str_data type : {}'.format(type(str_data)))
    print('flag_data type : {}'.format(type(flag_data)))
    print('none_data type : {}'.format(type(none_data)))
    print('PI type : {}'.format(type(PI)))
    print('list_data type : {}'.format(type(list_data)))
    print('tuple_data type : {}'.format(type(tuple_data)))
    print('dict_data type : {}'.format(type(dict_data)))
    print('set_data type : {}'.format(type(set_data)))
    print('json_data type : {}'.format(type(json_data)))
    print('json_01 type : {}'.format(type(json_01)))
    print('json_02 type : {}'.format(type(json_02)))

if __name__ == '__main__':
    data_type()
    # exception_test()
    # print_test()