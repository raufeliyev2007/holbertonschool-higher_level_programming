#!/usr/bin/python3
"""Comment"""
import urllib.request
import urllib.error
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
