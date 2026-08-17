#!/usr/bin/env bash
# Sends the correct request to /catch_me to trigger the success message
curl -s -X <METHOD> "0.0.0.0:5000/catch_me"
