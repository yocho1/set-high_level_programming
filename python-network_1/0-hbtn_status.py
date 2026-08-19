#!/usr/bin/python3
"""Script that fetches the hbtn status endpoint."""
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(
                "https://alx-intranet.hbtn.io/status") as response:
            body = response.read()
    except urllib.error.URLError:
        with urllib.request.urlopen(
                "https://intranet.hbtn.io/status") as response:
            body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
