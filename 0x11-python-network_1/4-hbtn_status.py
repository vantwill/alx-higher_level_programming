#!/usr/bin/python3
"""
requests model
"""

if __name__ == '__main__':
    import requests
    rslt = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(rslt.text.__class__))
    print("\t- content: {}".format(rslt.text))
