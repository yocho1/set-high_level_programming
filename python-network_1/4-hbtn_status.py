#!/usr/bin/python3
"""Script that fetches the hbtn status endpoint using requests."""
import requests

if __name__ == "__main__":
    try:
        response = requests.get(
            "https://alx-intranet.hbtn.io/status", timeout=5)
    except requests.exceptions.RequestException:
        response = requests.get("https://intranet.hbtn.io/status")
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
