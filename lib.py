import datetime
import requests
from collections import namedtuple

Title = namedtuple('Title', ['title', 'artist', 'date'])

class EmissionTitle:
    def __init__(self, title, album, artist, chapter):
        self.title = title
        self.artist = artist
        self.date = date

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

def print_titles(titles):
    for t in titles:
        print(t.date, t.title, t.artist)
