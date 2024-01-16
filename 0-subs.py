#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'})
    if res.status_code == 200:
        subs = res.json()
        return subs.get('data').get('subscribers')
    else:
        return (0)
