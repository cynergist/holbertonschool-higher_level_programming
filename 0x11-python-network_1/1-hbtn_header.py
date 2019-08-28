#!/usr/bin/python3
import urllib.request
import sys
'''
Script that takes in a URL, sends request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response
'''

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        ''' The returned response object gives us access to all headers '''
        print(response.getheader('X-Request-Id'))
