#!/bin/bash

# Check if URL and filename are provided as arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Set variables for URL and filename
url=$1
filename=$2

# Send JSON POST request with contents of file
curl -X POST -H "Content-Type: application/json" -d "@$filename" $url
