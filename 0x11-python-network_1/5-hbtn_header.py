#!/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url, auth=('user', 'pass'))
    if 'X-Request-ID' in req.headers:
        req_id = req.headers['X-Request-Id']
    print(req_id)
