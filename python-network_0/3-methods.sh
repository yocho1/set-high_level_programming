#!/usr/bin/env bash
# Displays all HTTP methods a server will accept for a given URL
curl -s -I -X OPTIONS "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
