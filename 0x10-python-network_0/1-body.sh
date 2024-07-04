#!/bin/bash

url=$1

response=$(curl -s -w "%{http_code}\n" "$url")

if [ "${response: -3}" = "200" ]; then
	curl -s "$url"
fi
