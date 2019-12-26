# -*- coding: utf-8 -*-

import requests

url = 'http://localhost:5000/ktm_predict'
r = requests.post(url,json={'Age':23, 'Gender':2, 'Occupation':4, 'Phone Type':3,'Current Bike':5,
                            'Relationship':4})

print(r.json())