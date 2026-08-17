#!/usr/bin/env bash
# Displays only the HTTP status code of the response for a given URL
curl -s -o /dev/null -w "%{http_code}\n" "$1"
