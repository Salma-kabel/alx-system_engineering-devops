#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces.
"""


import requests


def count_words(subreddit, word_list, after=None, count={}):
    """prints a sorted count of given keywords"""
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    res = requests.get(url, headers={"user-agent": "user"},
                       allow_redirects=False)
    for word in word_list:
        if word.lower() not in count.keys():
            count[word] = 0
    if res.status_code == 200:
        children = res.json().get("data").get("children")
        for child in children:
            title = child.get("data").get("title").lower().split(' ')
            for word in word_list:
                word = word.lower()
                count[word] += title.count(word)
        after = res.json().get("data").get("after")
        if after is None:
            result = []
            for key in count.keys():
                if count[key] != 0:
                    if result == []:
                        result.append("{}: {}".format(key, count[key]))
                    else:
                        for i in range(len(result)):
                            if count[key] > int(result[i].split(' ')[1]):
                                result = result[:i] + \
                                         ["{}: {}".format(key, count[key])] + \
                                         result[i:]
                                break
                            elif count[key] == int(result[i].split(' ')[1]):
                                list1 = [key, result[i].split(' ')[0]]
                                j = 1
                                while count[key] == int(result[i + j].split(
                                                            ' ')[1]):
                                    list1.append(result[i + j].split(' ')[0])
                                list1 = list1.sort
                                for j in range(len(list1)):
                                    if key == list1[j]:
                                        result = (result[:i + j] +
                                                  ["{}: {}".format(
                                                    key, count[key])]
                                                  + result[i + j:])
                            else:
                                continue
                else:
                    result.append("{}: {}".format(key, count[key]))
            if result != []:
                for re in result:
                    print(re)
            return
        return (count_words(subreddit, word_list, after, count))
