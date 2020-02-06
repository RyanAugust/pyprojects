import pandas as pd
import json
import datetime
import requests

api_key = 'f60ff71722196b2f8b766b94d94b6e91'

class flatten_json(object):
    def __init__(self, passed_json, delimiter='.'):
        self.passed_json = passed_json
        self.unpacked_json = {}
        self.delimiter = delimiter
    def constructor(self, passed_json, parent_key=''):
        for key, value in passed_json.items():
            full_key = self.key_maker(parent_key, key, self.delimiter)
            if type(value) == dict:
                kv_dict = self.constructor(value, full_key)
            else:
                kv_dict = {full_key: value}
            self.unpacked_json.update(kv_dict)
        return self.unpacked_json
    def key_maker(self, parent_key, key, delimiter):
        if parent_key != '':
            key = str(parent_key) + str(delimiter) + str(key)
        return key
    def flatten(self):
        return self.constructor(passed_json=self.passed_json)

def fetch_fred_data(api_key, series_id, start=datetime.datetime.today().strftime('%Y-%m-%d'), 
    end=datetime.datetime.today().strftime('%Y-%m-%d'),additional_params=None):
    url = 'https://api.stlouisfed.org/fred/series/observations'
    params = {'api_key':api_key,
    'file_type':'json',
    'series_id':series_id,
    'realtime_start':start,
    'realtime_end':end}
    if additional_params != None:
        params.update(additional_params)
    r = requests.get(url,params)
    assert r.status_code == 200, 'Invalid return'
    flat_json = [flatten_json(obs).flatten() for obs in r.json()['observations']]
    df = pd.DataFrame(flat_json)
    return df