#!/usr/bin/env bash
# Sends a PUT request to /catch_me to trigger the success message
curl -s -X PUT "0.0.0.0:5000/catch_me"
