#!/bin/bash

cd "$(dirname "$0")/data"

git add notes.md
git commit -m "Automated backup at $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
