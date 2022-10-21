#!/usr/bin/python3
'''
manage urllib.error.HTTPError exceptions and print Error codes
'''
import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as urls:
            print(urls.read().decode('utf-8'))
    except urllib.error.HTTPError as expt:
        error_code = str(expt).split(' ')[2][:-1]

        print("Error code: " + str(error_code))
