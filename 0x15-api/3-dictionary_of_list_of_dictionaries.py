#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import json
import requests


if __name__ == "__main__":
    """
    Main function of the script.
    Retrieves employee information and to-do list information using the
    REST API, and prints the to-do list progress for the employee.
    """

    # Base URL for the API endpoints
    url = "https://jsonplaceholder.typicode.com/"
    # Endpoint to get employee info
    user = requests.get(url + "users").json()
    # Endpoint to get todo list for the employee
    todos = requests.get(url + "todos").json()

    # Write the user to-do list information to a JSON file
    with open("todo_all_employees.json", "w") as JSONFile:
        # Write the information as a dictionary, with the key as the user ID
        # and the value as a list of dictionaries, each containing information
        # about a to-do task
        for dct in user:
            data = {dct.get("id"): [{
                "username": dct.get("username"),
                "task": t.get("title"),
                "completed": t.get("completed")
                 } for t in todos]}
            json.dump(data, JSONFile)
