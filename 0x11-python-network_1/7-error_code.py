#!/usr/bin/python3
'''
Takes the URL http://0.0.0.0:5000/ as argv[1] and sends a
request to the URL, and displays the body of the response
'''
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    if r.ok is True:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
'''
Example return:
$ ./7-error_code.py http://0.0.0.0:5000
Index
$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
'''
