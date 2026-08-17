#!/usr/bin/env bash
# Displays the body of a GET response only if the status code is 200
body=$(mktemp); code=$(curl -s -L -o "$body" -w "%{http_code}" "$1"); [ "$code" -eq 200 ] && cat "$body"; rm -f "$body"
