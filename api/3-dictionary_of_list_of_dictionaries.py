#!/usr/bin/python3
"""
This module exports all employees' tasks to a single JSON file.

The JSON file format must be:
{
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        ...
    ],
    "USER_ID": [
        ...
    ]
}

The file name is: todo_all_employees.json
"""

import json
import requests


if __name__ == "__main__":

    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Dictionary to store all data
    all_data = {}

    # Build JSON structure
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # List for this user's tasks
        user_tasks = []

        for todo in todos:
            if todo.get("userId") == user_id:
                user_tasks.append(
                    {
                        "username": username,
                        "task": todo.get("title"),
                        "completed": todo.get("completed")
                    }
                )

        all_data[str(user_id)] = user_tasks

    # Write to file
    file_name = "todo_all_employees.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(all_data, f)

    print("JSON file '{}' created.".format(file_name))
