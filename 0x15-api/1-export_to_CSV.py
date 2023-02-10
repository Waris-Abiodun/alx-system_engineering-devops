#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys
import csv

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
    # Open a new CSV file for writing with the name <user_id>.csv
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write a row to the CSV file for each task in the to-do list
        [writer.writerow(
            [sys.argv[1], username, dct.get("completed"), dct.get("title")])
         for dct in todos]

