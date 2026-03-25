#!/usr/bin/env python

import json
from datetime import datetime
import requests

## This script is used to generate the downloads badge for Avogadro
# We need to get the download data from SourceForge and GitHub
# (both avogadroapp and avogadrolibs)
#  and then write it to a badge for the README.md file

# get the download data from SourceForge first
start_date = "2006-04-14"
now = datetime.now().strftime("%Y-%m-%d")
r = requests.get(f'https://sourceforge.net/projects/avogadro/files/stats/json?start_date={start_date}&end_date={now}')

if r.status_code != 200:
    print("Error downloading SourceForge data")
    exit(1)

# parse the JSON
data = json.loads(r.text)

total_downloads = 0
for item in data['downloads']:
    date, downloads = item
    total_downloads += downloads

print("Total downloads from SourceForge:", total_downloads)

# now get the download data from GitHub
r = requests.get(f'https://api.github.com/repos/OpenChemistry/avogadrolibs/releases')

if r.status_code != 200:
    print("Error downloading GitHub data")
    exit(1)

# parse the JSON
data = json.loads(r.text)

avogadrolibs_downloads = 0
for release in data:
    for asset in release['assets']:
        avogadrolibs_downloads += asset['download_count']
total_downloads += avogadrolibs_downloads

print("Total avogadrolibs downloads from GitHub:", avogadrolibs_downloads)

# we also need to get the data from avogadroapp GitHub releases

r = requests.get(f'https://api.github.com/repos/OpenChemistry/avogadroapp/releases')

if r.status_code != 200:
    print("Error downloading GitHub data")
    exit(1)

# parse the JSON
data = json.loads(r.text)

avogadroapp_downloads = 0
for release in data:
    for asset in release['assets']:
        avogadroapp_downloads += asset['download_count']
total_downloads += avogadroapp_downloads

print("Total avogadroapp downloads from GitHub:", avogadroapp_downloads)

# human format with two decimals
dl_string = str(total_downloads)
if total_downloads > 1000000:
    dl_string = "{:.2f}M".format(total_downloads / 1000000)
elif total_downloads > 1000:
    dl_string = "{:.2f}K".format(total_downloads / 1000)

print("Total downloads:", dl_string)

# write this as a badge
r = requests.get(f"https://img.shields.io/badge/Downloads-{dl_string}-blue")

if r.status_code != 200:
    print("Error downloading badge")
    exit(1)

with open("downloads.svg", "w") as f:
    f.write(r.text)
