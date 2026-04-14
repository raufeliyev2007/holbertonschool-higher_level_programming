#!/usr/bin/python3
import requests
import sys

if len(sys.argv) > 2:
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
