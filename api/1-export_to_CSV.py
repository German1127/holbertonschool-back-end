#!/usr/bin/python3
"""Import Modules"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url_users = requests.get('https://jsonplaceholder.typicode.com/users')
    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    for i in url_users.json():
        if i['id'] == int(argv[1]):
            username = i['username']
    with open(f"{argv[1]}.csv", 'w') as f:
        for i in url_todos.json():
            if i['userId'] == int(argv[1]):
                completed = i['completed']
                title = i['title']
                f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".
                        format(argv[1], username, completed, title))
