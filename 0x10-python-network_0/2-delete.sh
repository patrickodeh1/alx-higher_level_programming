#!/bin/bash

url=$1

response=$(curl -s -X DELETE "$url")

echo "$response"
