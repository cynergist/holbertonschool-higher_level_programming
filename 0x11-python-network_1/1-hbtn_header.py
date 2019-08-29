#!/usr/bin/python3
'''
Takes in a URL, sends request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response
'''
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        ''' The returned response object gives us access to all headers '''
        print(response.getheader('X-Request-Id'))
'''
Example return:
$ ./1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
./1-hbtn_header.py https://intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
'''
