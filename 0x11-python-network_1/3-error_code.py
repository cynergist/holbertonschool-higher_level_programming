#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
'''
Script that takes in a URL, sends a request to the URL and,
displays the body of the response, decoded in utf-8
'''

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            ''' The returned response object gives us access to all headers '''
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
