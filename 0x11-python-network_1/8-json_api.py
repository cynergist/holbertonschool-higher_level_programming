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
    # Make a post request with the parameter
    try:
        r = requests.post(url, data={'q': q})
        '''
        With a POST request, form data appears within the message
        body of the HTTP request
        '''
        to_json = r.json()
        # Check that our response returned objects from the API
        if 'id' in to_json and 'name' in to_json:
            print('[{}] {}'.format(to_json['id'], to_json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')

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
