#!/bin/sh -l

date

output=$(python3 app.py --TOKEN=$1 \
--CHAT_ID=$2 \
--MESSAGE=$3 \
--PARSE=$4)

echo "::set-output name=status::$output"