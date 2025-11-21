#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(emp_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)).json()

    name = user.get("name")
    done_tasks = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(name, len(done_tasks), len(todos)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
