#!/usr/bin/python3

"""
for a given employee ID, returns information
about his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    req_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    res = requests.get(req_url).json()
    name = res['username']
    req_url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            argv[1])
    res2 = requests.get(req_url2).json()
    tasks = []
    dic1 = {}
    for task in res2:
        dic2 = {}
        dic2["task"] = task["title"]
        dic2["completed"] = task["completed"]
        dic2["username"] = name
        tasks.append(dic2)
    dic1[argv[1]] = tasks
    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump(dic1, f)
