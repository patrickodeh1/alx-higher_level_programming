#!/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    headers = {'Accept': 'application/vnd.github.v3+json'}

    try:
        r = requests.get(url, auth=(username, password), headers=headers)
        if r.status_code == 200:
            user_data = r.json()
            print(user_data['id'])
        else:
            print(None)

    except requests.exceptions.RequestException as e:
        print(None)
