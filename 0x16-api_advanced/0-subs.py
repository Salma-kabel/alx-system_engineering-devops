#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
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
    url = "https://oauth.reddit.com/r/{}/about/.json".format(subreddit)
    res = requests.get(url, headers={"user-agent": "SalmaSalahk",
                                     'Authorization': f'bearer {token}'},
                       allow_redirects=False)
    if res.status_code == 200:
        subs = res.json()
        return subs.get('data').get('subscribers')
    else:
        return (0)
