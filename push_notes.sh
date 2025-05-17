#!/bin/bash
cd /var/lib/docker/volumes/notes_data/_data
git add notes.json
git commit -m "Daily backup at $(date)"
git push origin main
