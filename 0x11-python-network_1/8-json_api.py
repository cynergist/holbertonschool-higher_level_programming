#!/usr/bin/python3
'''
Script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user, with the letter as parameter.
'''
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': ''}
    if len(argv) > 1:  # Get address from command line
        params['q'] = argv[1]  # Add value at argv[1] to our 'q' key
    r = requests.post(url, params=params)
    '''
    With POST, form data appears within the message body of the HTTP request
    '''
    try:
        body = r.json()
        if body is False:
            print('No result')
        else:
            print('[{}] {}'.format(body.get('id'), body.get('name')))
    except Exception:
        print('Not a valid JSON')

'''
Example return:
$ ./8-json_api.py
No result
$ ./8-json_api.py a
[8446] amnirqhtfjq
$ ./8-json_api.py 2
No result
$ ./8-json_api.py b
[7094] bmofakakhke
'''
