#!/usr/bin/python3
import requests
'''
Using only the package requests, this script fetches
https://intranet.hbtn.io/status
'''
if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}".format(r.text))
    print("\t- content: {}".format(r.headers['content-type']))
