#!/usr/bin/python3
'''
Script that takes in a URL and an email, sends a post request,
to the passed URL w/ email as param, and displays the body of the response
'''
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = dict(email=argv[2])

    data = urllib.parse.urlencode(values).encode('utf-8')
    r = urllib.request.Request(url, data)

    with urllib.request.urlopen(r) as response:
        ''' The returned response object gives us access to all headers '''
        url_page = response.read()
        print(url_page.decode())
'''
Returns:
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
'''
