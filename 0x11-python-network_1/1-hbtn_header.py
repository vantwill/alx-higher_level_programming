#!/usr/bin/python3
'''
displays the value of the X-Request-Id variable
'''
if __name__ == '__main__':
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as rens:
        print(rens.info()['X-Request-Id'])
