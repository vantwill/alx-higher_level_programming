#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id
'''
import requests
from sys import argv
if __name__ == "__main__":
    respns = requests.get(argv[1])
    print(respns.headers.get('x-request-id'))
