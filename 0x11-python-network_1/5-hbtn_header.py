#!/usr/bin/python3
'''
Sends request to https://intranet.hbtn.io/ and displays the value of the
X-Request-ID in the response header
'''
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-ID'))
