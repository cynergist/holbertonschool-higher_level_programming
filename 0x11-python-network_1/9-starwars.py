#!/usr/bin/python3
''' Script takes string and sends a search request to the Star Wars API '''
from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    # Search parameter is our line argument
    parameters = {'search': argv[1] if len(argv) > 1 else ''}
    # Make a get request with the parameters
    r = requests.get(url, params=parameters)
    # Convert to json format
    body = r.json()
    print('Number of results: {}'.format(body.get('count')))
    # Check that our response returned an object from the API
    if body is not None:
        for attr in body.get('results'):
            if attr.get('name'):
                print(attr.get('name'))
    else:
        print('body is a NoneType object -- Check Star Wars API URL')

'''
Output examples:
$ ./9-starwars.py r2
Number of results: 1
R2-D2
$ ./9-starwars.py g
Number of results: 16
Leia Organa
Biggs Darklighter
Greedo
Wedge Antilles
IG-88
Qui-Gon Jinn
Nute Gunray
Rugor Nass
Gasgano
Adi Gallia
'''
