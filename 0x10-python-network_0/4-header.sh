#!/bin/bash
# Send a GET request with custom header
curl -s -H "X-School-User-Id: 98" "$1"
