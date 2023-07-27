#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests as req
from sys import argv as arg


def getData():
    """
    Script to reurn a given employee ID, returns information
    about his/her TODO list progress."""

    users_list = req.get('https://jsonplaceholder.typicode.com/users').json()
    tasks_list = req.get('https://jsonplaceholder.typicode.com/todos').json()
    tasks_done = 0
    total_number_tasks = 0
    tasksDescription = []

    for users in users_list:
        if users.get('id') == int(arg[1]):
            user = users.get('name')
            break
    for tasks in tasks_list:
        if tasks.get('userId') == int(arg[1]):
            total_number_tasks += 1
            if tasks.get('completed') is True:
                tasks_done += 1
                tasksDescription.append(tasks.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        user, tasks_done, total_number_tasks))
    for des in tasksDescription:
        print("\t {}".format(des))


if __name__ == '__main__':
    getData()
