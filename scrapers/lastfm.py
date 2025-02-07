#!/usr/bin/env python3

import csv
from lib import get
import os
import re
import sys
import time
import functools

CSV_SEP = '\x1F'
TAG_SEP = '\x1E'
API_KEY = os.environ['LASTFM_API_KEY']
CLEANER = re.compile('\([^\(\)]+\)')


def cleaner(elem):
    elem = CLEANER.sub('', elem)
    return elem.strip()


def check_error(json):
    error = json.get('error')

    return error is not None


def extract_tags(json):
    error = json.get('error')

    if error is not None and error == 6:
        return []

    json_toptags = json['toptags']

    tags = [json_tag['name'] for json_tag in json_toptags['tag']
            if json_tag['count'] >= 10]

    return tags


def tags_for_artist(artist):
    assert len(artist) > 0, "Need an artist name!"

    req = get('http://ws.audioscrobbler.com/2.0/', params={
        'method': 'artist.gettoptags',
        'artist': artist,
        'autocorrect': 1,
        'api_key': API_KEY,
        'format': 'json',
    })

    json = req.json()
    tags = None

    if check_error(json):
        tags = []
    else:
        tags = extract_tags(req.json())

    return tags


@functools.lru_cache(maxsize=None)
def get_elems(track, artist):
    time.sleep(1/4)  # Last.fm rate limiting

    if not len(artist) > 0:
        print("Need an artist name!")
        return None

    if not len(track) > 0:
        print("Need a track name!")
        return None

    req = get('http://ws.audioscrobbler.com/2.0/', params={
        'method': 'track.gettoptags',
        'artist': artist,
        'track': track,
        'autocorrect': 1,
        'api_key': API_KEY,
        'format': 'json',
    })

    json = req.json()

    if check_error(json):
        return date, track, artist, TAG_SEP.join(tags_for_artist(artist))

    json_attr = json['toptags']['@attr']
    artist = json_attr['artist']
    track = json_attr['track']
    tags = extract_tags(req.json())

    if len(tags) == 0:
        print(track, "has no tags, search by artist!")
        tags = tags_for_artist(artist)

    return date, track, artist, TAG_SEP.join(tags)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage:", sys.argv[0], "<infile> <outfile> [line number]")
        sys.exit(1)

    with open(sys.argv[1], "r") as inpt:
        with open(sys.argv[2], "a") as out:
            reader = csv.reader(inpt, delimiter=CSV_SEP)
            writer = csv.writer(out, delimiter=CSV_SEP)
            i = 1

            for line in reader:
                try:
                    if len(sys.argv) > 3:
                        # We have already processed x lines
                        if i < int(sys.argv[3]):
                            i += 1
                            continue

                    if len(line) < 3:
                        print(line, "is invalid")
                        continue

                    date = line[0]
                    artist = cleaner(line[2])
                    track = cleaner(line[1])

                    line = get_elems(track, artist)

                    if line is None:
                        print(track, "-", artist, "not found!")
                        continue

                    writer.writerow(line)

                    if i % 2000 == 0:
                        print("Processed %d" % (i))

                    i = i + 1
                except:
                    print(line, "encountered an error:", sys.exc_info()[1])
