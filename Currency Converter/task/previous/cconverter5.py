import requests
import json

get_cur = input()
r = requests.get(f'http://www.floatrates.com/daily/{get_cur}.json')
jres = json.loads(r.content)

for cur in ['usd', 'eur']:
    print(jres.get(cur))
