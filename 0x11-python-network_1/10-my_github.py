#!/usr/bin/python3
''' Script takes Github credentials, uses the Github API to display 'id' '''
import requests
from sys import argv

if __name__ == '__main__':

    '''
    Per https://developer.github.com/v3/#basic-authentication
    all data is sent and received as JSON
    '''
    url = 'https://api.github.com/user'
    # Command line args are username and password, respectively
    r = requests.get(url, auth=(argv[1], argv[2]))
    jsonify = r.json()
    if 'id' in jsonify:
        print(jsonify['id'])
    else:
        print(None)

'''
Example output:
$ ./10-my_github.py cynergist cisfun
2531536
$ ./10-my_github.py cynergist wrong_pwd
None
'''
