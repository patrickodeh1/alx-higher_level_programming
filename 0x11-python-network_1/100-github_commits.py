#!/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    name = sys.argv[2]

    url = f'https://api.github.com/repos/{name}/{repo}/commits'
    params = {
        'per_page': 10,
        'page': 1,
    }
    headers = {'Accept': 'application/vnd.github.v3+json'}

    try:
        r = requests.get(url, params=params, headers=headers)
        r.raise_for_status()
        commits = r.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
