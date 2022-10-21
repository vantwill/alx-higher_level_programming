#!/usr/bin/python3
'''
use the GitHub API to display your id
'''
import requests
from sys import argv
if __name__ == "__main__":
    respo = requests.get('https://api.github.com/user',
                            auth=(argv[1], argv[2]))
    if "json" not in respo.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        respo = respo.json()
        print(respo.get('id'))
