#!/usr/bin/python3
"""
Script to retrieve employee TODO list progress using a REST API.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch employee data
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetch employee's todo list
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])

        # Display progress
        print(f"Employee {user_data['name']} is done with"
              f"tasks({completed_tasks}/{total_tasks}):")
        for todo in todos_data:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
