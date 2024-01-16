#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """gets 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers={"user-agent": "SalmaSalahk"},
                       allow_redirects=False)
    if res.status_code == 200:
        children = response.json().get('data').get('children')
        for child in range(10):
            print(children[child].get('data').get('title'))
    else:
        print("None")
