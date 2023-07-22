# Automatically updated Mastodon Infosec CSV file
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
