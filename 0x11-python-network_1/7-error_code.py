#!/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        r = requests.get(url, auth=('user', 'pass'))
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(r.status_code))
