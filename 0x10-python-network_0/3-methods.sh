#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

curl -I -X OPTIONS $1 | grep "Allow" | awk '{print $2}'
