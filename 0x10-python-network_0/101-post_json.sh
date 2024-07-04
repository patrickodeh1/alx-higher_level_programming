#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
