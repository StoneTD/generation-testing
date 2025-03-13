#!/bin/bash

echo "==============="

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.emal "${INPUT_EMAIL}"
git config --gloabl --add safe.directory /github/workspace

python3 /usr/bin/feed.py

git add . && git commit -m "Update Feed"
git push --set-upstream origin main

echo "==============="