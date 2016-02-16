#!/usr/bin/env python3

import http.client, urllib.request, urllib.parse
import json
import ast

filename = 'bulbasaur.txt'

def http_get(main_url, request, path):
    conn = http.client.HTTPConnection(main_url)
    conn.request(request, urllib.parse.quote(path))
    response = conn.getresponse()
    if response.status == 200:
        data = response.read()
        return data
    else:
        raise Exception("HTTP call failed: " + response.reason)

url = 'pokeapi.co'
hR = '/api/v1/pokedex/1/'
data = http_get(url, "GET", hR).decode('ascii')
data_dict = ast.literal_eval(data)

for k in data_dict['pokemon']:
    pkmn_name = k['name']
    pkmn_num = (k['resource_uri'].split('/'))[3]
    print(pkmn_num, pkmn_name)

#f = open(filename, 'w')
#json.dump(data, f)
#f.close()
