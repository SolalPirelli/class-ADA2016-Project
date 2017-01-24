#!/usr/bin/env python3

import datetime
import time

from lib import *

def extract_json_elem(json):
    title = json['title'].capitalize()
    artist = json['interpret'].capitalize()
    date = datetime.datetime.strptime(json['playtime'], '%Y-%m-%dT%H:%MZ')

    yield Title(title, artist, date)

def extract_json(json):
    for e in json['played']:
        yield from extract_json_elem(e)

def get_and_sleep_if_needed(url):
    while True:
        req = get(url)
        json = req.json()

        if isinstance(json, list):
            time.sleep(json[0]['time'])
            continue

        return json

def get_titles(dates):
    last_elem_yield = None
    for day in dates:
        last_time = datetime.time(0, 0, 0)
        while True:
            d = datetime.datetime.combine(day, last_time)
            url = 'http://www.onefm.ch/onair/playlist_query.php?dates={}'.format(d.strftime('%Y-%m-%d_%H:%M:%S'))

            json = get_and_sleep_if_needed(url)
            elems = list(extract_json(json))

            to_break = False
            for e in elems:
                if e == last_elem_yield:
                    continue

                t = e.date.time()
                if t >= last_time:
                    last_time = t
                    last_elem_yield = e
                    yield e
                else:
                    to_break = True
                    break

            if to_break:
                break

        break

print_titles(get_titles(dates_from_today()))
