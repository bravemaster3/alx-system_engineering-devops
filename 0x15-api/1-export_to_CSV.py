#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
export data in the CSV forma
"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(base_url+"users/"+user_id).json()
    all_todos = requests.get(base_url+"todos",
                             params={"userId": user_id}).json()
    print(type(user_info))
    csv_name = f"{user_id}.csv"
    with open(csv_name, 'wb') as out_file:
        csv_writer = csv.writer(out_file)
        for row in user_info:
            csv_writer.writerow(row.values())

    # print(user_todos)
