#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import random


FORTUNE_API_URL = 'http://www.yerkee.com/api/fortune'
# This is a random comment
# That's a comment!
"""
This is a docstring
"""
"""
This is another docstring
"""

class Fortune(object):
    def __init__(self, amount=1):
        self.amount = amount

    def _fetch_fortune(self):
        fortunes = []
        for _ in range(self.amount):
            r = requests.get(FORTUNE_API_URL)
            one_fortune = r.json()
            fortunes.append(one_fortune['fortune'])
        return fortunes

    def give_me_my_fortune(self):
        return(self._fetch_fortune())


if __name__ == '__main__':
    my_fortune = Fortune()
    fortunes = my_fortune.give_me_my_fortune()
    for this_fortune in fortunes:
        print(this_fortune)
