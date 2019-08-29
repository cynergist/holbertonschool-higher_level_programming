#!/usr/bin/python3
'''
Script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user, with the letter as parameter.
'''
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    # q parameter is our line argument
    q = argv[1] if len(argv) > 1 else ''
    # Make a post request with the parameter and convert to json
    r = requests.post(url, data={'q': q}).json()
    '''
    With POST, form data 'id' and 'name' appear within the message body
    of the HTTP request upon converting to json
    '''
    if 'id' in r or 'name' in r is not None:
        print('[{}] {}'.format(r['id'], r['name']))
    # Check that our response returned objects from the API
    elif 'id' in r or 'name' in r is None:
        print('Not a valid JSON')
    else:
        print('No result')

'''
Example output:
$ ./8-json_api.py
No result
$ ./8-json_api.py a
[8446] amnirqhtfjq
$ ./8-json_api.py 2
No result
$ ./8-json_api.py b
[7094] bmofakakhke
'''
