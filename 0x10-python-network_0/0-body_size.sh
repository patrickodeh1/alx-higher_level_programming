#!/bin/bash

url=$1

size=$(curl -s -o /dev/null -w "%{size_download}\n" "$url")

echo "$size"
