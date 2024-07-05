#!/usr/bin/python3
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status\
    ', auth=('user', 'pass'))
    body = r.text
    print("Body response: ")
    print("\t - type: {}".format(type(body)))
    print("\t - content: {}".format(body))
