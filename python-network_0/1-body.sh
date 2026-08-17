#!/usr/bin/env bash
# Displays the body of a GET response only if the status code is 200
status=$(curl -s -o /tmp/response_body -w "%{http_code}" "$1")
if [ "$status" -eq 200 ]; then
    cat /tmp/response_body
fi
