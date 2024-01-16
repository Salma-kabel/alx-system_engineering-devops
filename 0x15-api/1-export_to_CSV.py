#!/usr/bin/python3

"""
for a given employee ID, returns information
about his/her TODO list progress.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    req_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    res = requests.get(req_url).json()
    name = res['name']
    req_url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            argv[1])
    res2 = requests.get(req_url2).json()
    tasks = []
    for task in res2:
        tasks.append([argv[1], name, task['completed'], task['title']])
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)
