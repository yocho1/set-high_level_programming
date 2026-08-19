#!/usr/bin/python3
"""Script that sends a POST request with an email parameter."""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    req = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(body.decode("utf-8"))
