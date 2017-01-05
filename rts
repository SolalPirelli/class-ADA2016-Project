#!/usr/bin/env python3

import datetime
import re
import sys

from lib import *

NAME, = sys.argv[1:]
BASE_URL = 'https://www.rts.ch/{}'.format(NAME)

def get_titles_basic(dates):

    def datetime_from_node(date, node):
        return datetime.datetime.combine(
            date,
            datetime.datetime.strptime(node.text, '%H:%M:%S').time(),
        )

    for d in dates:
        url = BASE_URL + '/quel-titre/'
        params = {
            'd': d.strftime('%d/%m/%Y'),
            'dh': '00',
            'dm': '00',
        }
        req = get(url, params=params)

        soup = bs(req.text)
        for item in soup.find_all('table', id='tableSelection_content')[1:]:
            node_time, node_artist, node_title = item.find_all('td')
            date = datetime_from_node(d, node_time)

            yield Title(node_title.text, node_artist.text, date)

def get_titles_couleur3(dates):

    def datetime_from_node(date, node):
        return datetime.datetime.combine(
            date,
            datetime.datetime.strptime(node.text, '%H:%M').time(),
        )

    for d in dates:
        url = '{}/quel-titre/?date={}'.format(BASE_URL, d.strftime('%d-%m-%Y'))
        req = get(url)

        soup = bs(req.text)
        for item in soup.find_all('div', class_='item'):
            node_title, node_artist, node_time = item.find_all('span')
            date = datetime_from_node(d, node_time)

            yield Title(node_title.text, node_artist.text, date)

def get_index_of_today(emission):
    url = '{}/programmes/{}'.format(BASE_URL, emission)
    req = get(url)

    soup = bs(req.text)
    calendar = soup.find(id='detailed-calendar')
    today_node = calendar.find(class_='today')

    today_re = re.compile('.*/(\\d+)-[a-z\\d-]+.html')
    today_match = today_re.match(today_node.a['href'])
    if not today_match:
        raise KeyError('Unable to find today index')

    return int(today_match.group(1))

def get_dates_in_calendar(date, soup):
    yield (date, 123)

def playlist_of_emission_index(emission, index):
    url = '{}/programmes/{}/{}.html'.format(BASE_URL, emission, index)
    req = get(url)

    soup = bs(req.text)
    program = soup.find(class_='musical-program')
    for item in program.find_all('li', class_='opa-50'):
        node_title, node_album, node_artist, node_time = item.find_all('span')
        date = datetime_from_node(d, node_time)

        yield Title(node_title.text, node_album.text, node_artist.text, date)


def dates_to_index_of_emission(emission):
    index = get_index_of_today(emission)

    url = '{}/programmes/{}/?format=radio/couleur3/get-calendar&type=bcst&idbcst={}'.format(
        BASE_URL, emission, index # TODO couleur3 is hardcoded, issue?
    )
    req = get(url)

    yield from get_dates_in_calendar(datetime.date.today(), bs(req.text))


def get_titles_for_emission(dates, emission):
    for d in dates:
        url = '{}/programmes/'.format(BASE_URL, emission)
        req = get(url)

get_titles_map = {
    'la-1ere': get_titles_basic,
    'espace-2': get_titles_basic,
    'couleur3': get_titles_couleur3,
    'option-musique': get_titles_basic,
}
get_titles = get_titles_map[NAME]

dump_titles(get_titles(dates_from_today()))

#print(list(dates_of_emission('electro-libre')))

#for t in get_titles_for_emission(dates_from_today(), 'downtown-boogie'):
    #print(t.date, t.title, t.album, t.artist)
