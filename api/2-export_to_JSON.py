#!/usr/bin/python3
"""
This module exports all tasks owned by a specific user into a JSON file.

The JSON file format must be:
{
    "USER_ID": [
        {
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS,
            "username": "USERNAME"
        },
        ...
    ]
}

The file name is: USER_ID.json
"""

import json
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    # Build URLs
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    user_data = requests.get(user_url).json()
    username = user_data.get("username")

    # Fetch all todos
    todos = requests.get(todos_url).json()

    # Create list of task dictionaries
    tasks_list = []
    for todo in todos:
        if todo.get("userId") == user_id:
            tasks_list.append(
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
                }
            )

    # Structure for JSON export
    json_data = {str(user_id): tasks_list}

    # File name
    file_name = "{}.json".format(user_id)

    # Write to JSON file
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(json_data, f)

    print("JSON file '{}' created.".format(file_name))
