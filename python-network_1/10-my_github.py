#!/usr/bin/python3
import requests
import sys
from requests.auth import HTTPBasicAuth

if len(sys.argv) > 2:
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    r = requests.get(url, auth=HTTPBasicAuth(username, password))

    try:
        json_data = r.json()
        if r.status_code == 200:
            print(json_data.get('id'))
        else:
            print("None")
    except ValueError:
        print("None")
