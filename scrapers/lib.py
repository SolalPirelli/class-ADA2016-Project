import datetime
import requests
from collections import namedtuple
from bs4 import BeautifulSoup as BeautifulSoup

SEP = '\x1F'
bs = lambda t: BeautifulSoup(t, 'lxml')

Title = namedtuple('Title', ['title', 'artist', 'date'])

def dates_from_today():
    old = datetime.date.today()
    yield old

    while True:
        new = old - datetime.timedelta(days=1)
        yield new
        old = new

session = requests.Session()
def get(url, **kwargs):
    req = session.get(url, **kwargs)
    assert req.status_code == 200

    return req

def post(url, **kwargs):
    req = session.post(url, **kwargs)
    assert req.status_code == 200

    return req

def print_titles(titles):
    for t in titles:
        print(t.date, t.title, t.artist)

def dump_titles(titles):
    for t in titles:
        print('{}{}{}{}{}'.format(t.date, SEP, t.title, SEP, t.artist))
