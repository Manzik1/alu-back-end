#!/usr/bin/python3

"""Import libraries"""
import requests
import sys
import csv

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    # Fetch data
    todo_data = requests.get(todos_url).json()
    user_data = requests.get(users_url).json()

    employee_name = user_data["username"]

    # Prepare CSV file name
    file_name = "{}.csv".format(user_id)

    # Open CSV file and write data
    with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todo_data:
            if todo["userId"] == user_id:
                writer.writerow([
                    user_id,
                    employee_name,
                    todo["completed"],
                    todo["title"]
                ])

    print("CSV file '{}' has been created.".format(file_name))
