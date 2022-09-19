#!/bin/sh -l

date

python3 app.py --TOKEN=$1 \
--CHAT_ID=$2 \
--MESSAGE=$3 \
--PARSE=$4