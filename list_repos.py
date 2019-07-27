# list_repos.py

# Script to list the Github repos of a given user, with their urls
# Author: John Lynch (@teraspora)
# July 27th 2019

import json, urllib.request

username = input('\u001B[91mEnter username:\n    \u001B[96m')
print('\u001B[91m\n')
url = f'https://api.github.com/users/{username}/repos'
repos = json.loads(urllib.request.urlopen(url).read())

for repo in repos:
    print(f'{repo["name"]} - {repo["html_url"]}')
