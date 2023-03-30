#!/bin/bash

# Check if URL is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the size of the response body in bytes
response_size=$(curl -s -w '%{size_download}' -o /dev/null "$1")

# Display the size of the response body
echo "Size of the response body: ${response_size} bytes"
