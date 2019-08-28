#!/usr/bin/python3
''' A Python script that fetches https://intranet.hbtn.io/status '''

import urllib.request
import urllib.parse
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
    print("Body response:\n\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf-8')))
