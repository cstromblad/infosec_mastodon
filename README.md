# Introduction
There are two primary files (curated_infosec.csv, and mastodon_infosec_import.csv) in this repository. Both contain people "identifying" as information and cybersecurity people. The masotdon_infosec_import.csv contain ALL people listed in the Lukasz spreadsheet document. The curated file has excluded people matching the following criteria:

1. No toots at all?
2. No toots in the last 3 months?
3. Less than 10 toots in total?
4. Following less than 5 accounts.
5. Following more than followers.
6. Less than 500 followers.

The full list contains (as of 2024-12-01) 548 accounts and the curated list 147 accounts. Only the total list CSV-file is automatically updated.

## Automatically updated Mastodon Infosec CSV file
This repository contains a CSV-file which is automatically updated every hour if any additions have been made. The [original source](https://docs.google.com/spreadsheets/d/1t13k5_cNhP9_TgoUmqDZk2ROkWkF6Bg3O5269vKIqWw/view) is maintained by [Lukasz Olejnik](https://mastodon.social/@LukaszOlejnik).

There is some level of variation on the input (what's in the sheets-document), and I've tried to (minimally) keep it clean from stuff.

# Building your own Docker image

First of all, I know almost nothing about Docker. The current Dockerfile is built by an amateur, trust it you NOT SHOULD.

1. Change all REPO-related stuff to your own.
2. Generate a new SSH-key specifically for this purpose.
3. Upload/create a new deployment key for your repository here at github.
4. Add your new ssh_deployment_key to the `files/` folder
5. Build the image.
6. Run the image.

That... SHOULD be it.

# Todo
- Graciously accept improvements to this wonderful Python artwork.
