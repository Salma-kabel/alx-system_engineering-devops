#!/usr/bin/python3

"""
for a given employee ID, returns information
about his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    req_url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(req_url).json()
    dic1 = {}
    for employee in res:
        req_url2 = "https://jsonplaceholder.typicode.com/users/{}/todos"
                    .format(employee['id'])
        res2 = requests.get(req_url2).json()
        tasks = []
        for task in res2:
            dic2 = {}
            dic2["username"] = employee['username']
            dic2["task"] = task["title"]
            dic2["completed"] = task["completed"]
            tasks.append(dic2)
        dic1[employee['id']] = tasks
    with open("todo_all_employees.json", 'w') as f:
        json.dump(dic1, f)
