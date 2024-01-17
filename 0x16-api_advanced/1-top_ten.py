#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """gets 10 hot posts listed for a given subreddit"""
    auth = requests.auth.HTTPBasicAuth('WsYGrVymVI9ASJxSjUjPow',
                                       'CXbId8lefeCG6l9h5xbrAm4HK7HHyQ')
    data = {
        'grant_type': 'password',
        'username': 'SalmaSalahk',
        'password': '213879546',
    }
    headers = {
        'User-Agent': 'python:Mandelbot v1.0.0 by /u/SalmaSalahk'
    }

    response = requests.post('https://www.reddit.com/api/v1/access_token',
                             auth=auth, data=data, headers=headers)
    token = response.json()['access_token']

    url = "https://oauth.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers={
        'User-Agent': 'python:Mandelbot v1.0.0 by /u/SalmaSalahk',
        'Authorization': f'bearer {token}'},
                       allow_redirects=False)

    if res.status_code == 200:
        children = res.json().get('data').get('children')
        for child in range(10):
            print(children[child].get('data').get('title'))
    else:
        print("None")
