#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import json
import requests
import sys

if __name__ == "__main__":
    """
    Main function of the script.
    Retrieves employee information and to-do list information using the
    REST API, and prints the to-do list progress for the employee.
    """

    # Base URL for the API endpoints
    url = "https://jsonplaceholder.typicode.com/"
    # Endpoint to get employee info
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    # Endpoint to get todo list for the employee
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    username = user.get("username")
    # Write the user to-do list information to a JSON file
    with open("{}.json".format(sys.argv[1]), "w") as JSONFile:
        # Write the information as a dictionary, with the key as the user ID
        # and the value as a list of dictionaries, each containing information
        # about a to-do task
        data = {sys.argv[1]: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todos]}

        json.dump(data, JSONFile)
