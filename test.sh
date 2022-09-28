#!/bin/bash


for i in $(git status | awk '{print $1}' | cut -f1 -d ":"); do
	if [ "$i" == "deleted" ]; then
		echo "$i   - files removed from local repo"
	elif [ "$i" == "Untracked" ]; then
		echo "$i - files added to local repo"
	fi
done
