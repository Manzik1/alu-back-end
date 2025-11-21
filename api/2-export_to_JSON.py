#!/usr/bin/python3
import json
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    # URLs
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    # Fetch data
    todo_data = requests.get(todos_url).json()
    user_data = requests.get(user_url).json()

    username = user_data.get("username")

    # Build list of task dictionaries
    tasks_list = []
    for todo in todo_data:
        if todo.get("userId") == user_id:
            task_dict = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            tasks_list.append(task_dict)

    # Final JSON structure
    output = {str(user_id): tasks_list}

    # Filename
    file_name = "{}.json".format(user_id)

    # Write to JSON file
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(output, json_file)

    print("JSON file '{}' has been created.".format(file_name))
