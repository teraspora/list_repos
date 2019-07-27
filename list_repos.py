# list_repos.py

# Script to list the Github repos of a given user, with their urls
# Author: John Lynch (@teraspora)
# July 27th 2019

import json, urllib.request

print('List a user\'s Github repositories...')
username = input('\u001B[91mEnter username:\n    \u001B[96m')
print('\u001B[91m')
urls = [f'https://api.github.com/users/{username}/repos?per_page=100&page={i}' for i in range(1, 11)]

print(f'\u001B[33mGithub Repositories for {username}:\u001B[91m\n')

for url in urls:
    repos = json.loads(urllib.request.urlopen(url).read())
    for repo in repos:
        print(f'{repo["name"]} - {repo["html_url"]}')
