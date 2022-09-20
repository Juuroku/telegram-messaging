#!/bin/sh -l

date

if [ -z "$4" ];
then
	output=$(python3 /usr/bin/app.py -t "$1" \
	-c "$2" \
	-m "$3");
;
else
	output=$(python3 /usr/bin/app.py -t "$1" \
	-c "$2" \
	-m "$3" \
	-p "$4");
fi

echo "::set-output name=status::$output"