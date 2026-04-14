#!/usr/bin/python3
import requests
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
