#!/bin/bash
url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"
curl -s -X POST -d "email=$email" -d "subject=$subject" "$url"
