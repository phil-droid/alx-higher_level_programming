#!/bin/bash

# Take in URL as argument
url=$1

# Send GET request and save response body to a variable
response=$(curl -s -o /dev/null -w "%{http_code}" $url)
if [ "$response" -eq 200 ]; then
  body=$(curl -s $url)
  echo $body
else
  echo "Error: Response status code was $response"
fi
