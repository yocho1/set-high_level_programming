#!/usr/bin/env bash
# Sends a GET request with an X-School-User-Id header and shows the body
curl -s -H "X-School-User-Id: 98" "$1"
