#!/usr/bin/python3
''' Script takes Github credentials, uses the Github API to display 'id' '''
import requests
from sys import argv

if __name__ == '__main__':

    '''
    Per https://developer.github.com/v3/#basic-authentication
    all data is sent and received as JSON
    '''
    url = 'https://api.github.com'
    # Command line args are username and password, respectively
    r = requests.get(url, auth=(argv[1], argv[2]))

    jsonify = r.json()

    print(jsonify.get('id'))

'''
Example output:
$ ./10-my_github.py papamuziko cisfun
2531536
$ ./10-my_github.py papamuziko wrong_pwd
None
'''
