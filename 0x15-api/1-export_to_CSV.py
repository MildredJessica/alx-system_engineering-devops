#!/usr/bin/python3
"""Export data in the CSV format"""

import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'
    user = get(url + userId).json()
    tasks = get(url + userId + '/todos/'.format(userId)).json()
    userName = user.get('username')
    with open("{}.csv".format(userId), "w", newline='') as csvfile:
        file = csv.writer(
            csvfile, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            file.writerow([
                userId, userName,
                task.get('completed'), task['title']])
