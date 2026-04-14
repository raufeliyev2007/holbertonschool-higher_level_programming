#!/usr/bin/python3
"""Comment"""
import urllib.request
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
