#!/usr/bin/python3
'''
Takes the URL http://0.0.0.0:5000/post_email as argv[1] and
hr@holbertonschool.com as argv[2], sends a POST request with email as param,
and displays the body of the response
'''
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.post(argv[1], dict(email=argv[2]))
    print(r.text)
