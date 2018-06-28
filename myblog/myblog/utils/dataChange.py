# coding=utf8

from __future__ import print_function, absolute_import, division
import pandas as pd
import numpy as np
import json
import requests
import decimal
import cdecimal
import datetime


def json_merge(js_model, js_type):
    dict_input = {
        'js_model': js_model,
        'js_type': js_type
    }
    js_input = json.dumps(dict_input)
    return js_input


def json_split(js_input):
    dict_input = json.loads(js_input)
    return dict_input['js_model'], dict_input['js_type']


def dict_to_json(dict_model, ensure_ascii=False):
    return json.dumps(pd_to_json(dict_model), ensure_ascii=ensure_ascii)


def pd_to_json(dict_model):
    for k in dict_model.keys():
        if isinstance(dict_model[k], dict):
            dict_model[k] = pd_to_json(dict_model[k])
        elif isinstance(dict_model[k], pd.DataFrame):
            if dict_model[k].empty:
                pass
            else:
                #dict_model[k] = dict_model[k].fillna('')
                for field in dict_model[k].columns:
                    if isinstance(dict_model[k][field].iloc[0], cdecimal.Decimal):
                        dict_model[k][field] = dict_model[k][field].apply(
                            lambda x: decimal.Decimal(float(x)).quantize(decimal.Decimal('0.0000'))
                        )
                    if isinstance(dict_model[k][field].iloc[0], datetime.datetime):
                        dict_model[k][field] = dict_model[k][field].apply(
                            lambda x: x.isoformat()
                        )
            dict_model[k] = dict_model[k].to_dict(orient='records')
            #dict_model[k] = dict_model[k].to_json(orient='records', date_format='iso', force_ascii=0)
        # 如果是 numpy 的类型
        elif type(dict_model[k]).__module__ == np.__name__:
            dict_model[k] = dict_model[k].item()
        else:
            pass
    return dict_model


def json_to_dict(js_input):
    dict_model = json.loads(js_input)
    return pd_to_dict(dict_model)


def pd_to_dict(dict_model):
    if not isinstance(dict_model, dict):
        return dict_model
    for k in dict_model.keys():
        if isinstance(dict_model[k], list) \
                and set(map(lambda x: isinstance(x, dict), dict_model[k])) == set([True]):
            dict_model[k] = pd.DataFrame(dict_model[k])
        else:
            dict_model[k] = pd_to_dict(dict_model[k])
    return dict_model


def dict_to_json_bak(dict_model):
    for k in dict_model.keys():
        if isinstance(dict_model[k], dict):
            dict_model[k] = dict_to_json_bak(dict_model[k])
        elif isinstance(dict_model[k], pd.DataFrame):
            if dict_model[k].empty:
                pass
            else:
                for field in dict_model[k].columns:
                    if isinstance(dict_model[k][field].iloc[0], cdecimal.Decimal):
                        dict_model[k][field] = dict_model[k][field].apply(
                            lambda x: decimal.Decimal(float(x)).quantize(decimal.Decimal('0.0000'))
                        )
            dict_model[k] = dict_model[k].to_json(orient='records', date_format='iso', force_ascii=0)
        # 如果是 numpy 的类型
        elif type(dict_model[k]).__module__ == np.__name__:
            dict_model[k] = dict_model[k].item()
        else:
            pass
    return json.dumps(dict_model)


def json_to_dict_bak(js_input):
    dict_model = json.loads(js_input)
    for k in dict_model.keys():
        try:
            dict_model[k] = json_to_dict_bak(dict_model[k])
        except:
            try:
                dict_model[k] = pd.read_json(dict_model[k])
            except Exception as e:
                pass
    return dict_model


def post_json(js, url):
    headers = {'content-encoding': 'utf-8', 'content-type': 'application/json'}
    return requests.post(url=url,
                         data=js,
                         headers=headers,
                         timeout=30
                         ).content



if __name__ == '__main__':
    print(pd.__version__)
    print(np.__version__)