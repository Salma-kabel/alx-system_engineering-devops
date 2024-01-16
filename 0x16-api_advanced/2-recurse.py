#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """gets all hot articles for a given subreddit."""
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    res = requests.get(url, headers={"user-agent": "user"},
                                  allow_redirects=False)
    if res.status_code == 200:
        articles = res.json()
        children = articles.get("data").get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))
        after = articles.get("data").get("after")
        if after is None:
            return hot_list
        return (recurse(subreddit, hot_list, after))
    return None
