"""Export data in the JSON format"""
#!/usr/bin/python3

import csv
from requests import get
from sys import argv
import json


if __name__ == "__main__":
    userId = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'
    user = get(url + userId).json()
    tasks = get(url + userId + '/todos/'.format(userId)).json()
    userName = user.get('username')
    with open("todo_all_employees.json".format(userId), "w", newline='') as jsonfile:
    
        for task in tasks:
            json.dump({userId: [{
                "username": userName,
                "task": task['title'],
                "completed": task['completed'],
                
            }]}, jsonfile)
