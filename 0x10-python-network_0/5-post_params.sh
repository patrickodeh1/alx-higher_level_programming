#!/bin/bash

url=$1

response=$(curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$url")

echo "$response"
