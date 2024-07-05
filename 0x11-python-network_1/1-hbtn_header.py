#!/usr/bin/python3
"""header"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.getheaders()
        req_id = dict(headers).get('X-Request-Id')
    print(req_id)
