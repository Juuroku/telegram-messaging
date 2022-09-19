#!/bin/sh -l

date

output=$(python3 app.py --TOKEN=$INPUT_TELEGRAM-TOKEN \
--CHAT_ID=$INPUT_TELEGRAM-CHAT \
--MESSAGE=$INPUT_MESSAGE \
--PARSE=$INPUT_PARSE)

echo "::set-output name=status::$output"