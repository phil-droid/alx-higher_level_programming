#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

from sys import argv
from urllib.request import Request, urlopen

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
