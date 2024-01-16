#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""


import requests
import requests.auth



def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    CLIENT_ID = 'WsYGrVymVI9ASJxSjUjPow'
    CLIENT_SECRET = 'XbId8lefeCG6l9h5xbrAm4HK7HHyQ'
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    #post_data = {'grant_type': 'password', 'username': SalmaSalahk, 'password': 'PASSWORD'}
    headers = {
        'User-Agent': 'A Red automation script 1.1 by Jay'
        }
    TOKEN_ACCESS_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'
    response = requests.post(TOKEN_ACCESS_ENDPOINT, headers=headers, auth=client_auth)
    if response.status_code == 200:
        token_id = response.json()['access_token']

    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    res = requests.get(url, headers={"user-agent": "SalmaSalahk"},
                       allow_redirects=False)
    if res.status_code == 200:
        subs = res.json()
        return subs.get('data').get('subscribers')
    else:
        return (0)
