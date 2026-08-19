#!/usr/bin/python3
"""Script that displays a GitHub user's id using Basic Authentication."""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, password)
    )
    print(response.json().get("id"))
