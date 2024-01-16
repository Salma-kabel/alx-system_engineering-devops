#!/usr/bin/python3

"""
for a given employee ID, returns information
about his/her TODO list progress.
"""


import requests
from sys import argv


if __name__ == '__main__':
    req_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    res = requests.get(req_url).json()
    name = res['name']
    req_url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            argv[1])
    res2 = requests.get(req_url2).json()
    length = len(res2)
    tasks = []
    for task in res2:
        if task['completed']:
            tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(name,
                len(tasks), length))
    for task in tasks:
        print("{}".format(task['title']))
