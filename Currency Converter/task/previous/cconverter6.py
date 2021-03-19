from typing import Dict, Any

import requests
import json

class Exchanger:

    def __init__(self):
        self.main_cur = input().lower()
        r = requests.get(f'http://www.floatrates.com/daily/{self.main_cur}.json')
        self.jres: Dict[str, Dict[str, Any]] = json.loads(r.content)
        self.cache: Dict[str, float] = {}  # {to_currency: <the rate of from_currency for to_currency>}
        self.is_in_cache = False
        for curr in ['usd', 'eur']:
            self.parse_from_json_to_cache(curr)
        self.main_loop()

    def main_loop(self):
        to_cur = input()
        while len(to_cur.strip()):
            self.is_in_cache = False
            main_cur_sum = float(input())
            print('Checking the cache...')
            rate = self.check_cache(to_cur.lower())
            print('Oh! It is in the cache!' if self.is_in_cache else 'Sorry, but it is not in the cache!')
            print(f'You received {round(main_cur_sum * rate, 2)} {to_cur}.')
            to_cur = input()

    def parse_from_json_to_cache(self, to_curr: str) -> float:
        to_curr_dict = self.jres.get(to_curr)
        rate = to_curr_dict.get('rate') if to_curr_dict else 1  # in case of the same currency
        self.cache[to_curr] = rate
        return rate

    def check_cache(self, to_curr: str) -> float:
        self.is_in_cache = to_curr in self.cache
        if self.is_in_cache:
            return self.cache.get(to_curr)
        return self.parse_from_json_to_cache(to_curr)


Exchanger()
