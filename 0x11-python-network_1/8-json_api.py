#!/usr/bin/python3
"""json api"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    try:
        r = requests.post(url, data=data)
        r.raise_for_status()

        json_response = r.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")

    except requests.exceptions.HTTPError as e:
        print("No result")
    except ValueError:
        print("Not a valid JSON")
