#!/usr/bin/python3
"""
This module exports all employees' tasks to a single JSON file.

The JSON output format must be:
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

All users must appear in the output.
All tasks must be included and assigned to the correct user IDs.

The output file is: todo_all_employees.json
"""

import json
import requests


if __name__ == "__main__":

    # Endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users and todos
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Output dictionary
    all_data = {}

    # Create entry for every user (requirement: ALL users exist in output)
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Create an empty list for their tasks
        all_data[str(user_id)] = []

        # Assign all tasks belonging to this user (requirement: ALL tasks included)
        for todo in todos:
            if todo.get("userId") == user_id:
                all_data[str(user_id)].append(
                    {
                        "username": username,
                        "task": todo.get("title"),
                        "completed": todo.get("completed")
                    }
                )

    # Write to file
    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        json.dump(all_data, file)
