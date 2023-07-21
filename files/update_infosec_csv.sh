#!/bin/sh

cd /opt/infosec_mastodon
python3 /opt/infosec_mastodon.py
git add mastodon_infosec_import.csv
git commit -m "Automatically update CSV-file"
git push
