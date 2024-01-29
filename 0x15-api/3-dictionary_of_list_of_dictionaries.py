#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
export data in the JSON format.
"""

if __name__ == "__main__":
    import json
    import requests

    base_url = "https://jsonplaceholder.typicode.com/"

    all_users = requests.get(base_url+"users/").json()
    out_dict = {}
    for user in all_users:
        user_id = user.get('id')
        username = user.get('username')
        todos = requests.get(base_url+"todos",
                             params={"userId": user_id}).json()
        list_tasks = [{"task": todo.get('title'),
                       "completed": todo.get("completed"),
                       "username": username} for todo in todos]

        out_dict.update({user_id: list_tasks})

    json_name = "todo_all_employees.json"
    with open(json_name, 'w') as jsonfile:
        json.dump(out_dict, jsonfile)
