#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

url="$1"

curl -s -H "X-School-User-Id: 98" "$url"
