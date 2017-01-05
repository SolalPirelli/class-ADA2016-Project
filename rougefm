#!/usr/bin/env python3

from lib import *
import datetime
import string

def get_titles(dates):
    for d in dates:
        time = datetime.time.max

        found_next_day = False
        while not found_next_day:

            data = {
                'date': d.strftime('%Y-%m-%d'),
                'time': time.strftime('%H:%M'),
            }
            req = post('http://www.rougefm.com/playlist', data=data)

            soup = bs(req.text)
            for div in soup.find_all(class_='modal-body'):
                artist, title = div.find_all('b')
                date = datetime.datetime.strptime(div.small.text, 'Horaire de diffusion : %d/%m/%Y -  %H:%M')

                if date.date() < d:
                    found_next_day = True
                    break
                time = date.time()

                yield Title(
                    string.capwords(title.text),
                    string.capwords(artist.text),
                    date,
                )

dump_titles(get_titles(dates_from_today()))
