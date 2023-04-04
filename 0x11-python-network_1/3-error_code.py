#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import 

def get_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == '__main__':
    url = sys.argv[1]
    get_url_content(url)
