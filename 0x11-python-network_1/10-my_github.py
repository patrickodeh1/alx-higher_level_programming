#!/usr/bin/python3
"""github"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(username, password))
    user_data = r.json()
    print(user_data.get('id'))
