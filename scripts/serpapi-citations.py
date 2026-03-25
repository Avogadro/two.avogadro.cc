#!/usr/bin/env python

import requests
import os

# Get API key from environment variable
SERPAPI_KEY = os.environ.get('SERPAPI_KEY')
if not SERPAPI_KEY:
    print("Error: Please set SERPAPI_KEY environment variable")
    print("Get your API key at: https://serpapi.com/")
    exit(1)

# Search for the specific paper
params = {
    'engine': 'google_scholar',
    'q': 'Avogadro: an advanced semantic chemical editor, visualization, and analysis platform',
    'api_key': SERPAPI_KEY
}

response = requests.get('https://serpapi.com/search', params=params)

if response.status_code != 200:
    print(f"Error: API request failed with status {response.status_code}")
    exit(1)

data = response.json()

# Find the Avogadro paper and get citation count
num_citations = 0
paper_title = ""

if 'organic_results' in data and len(data['organic_results']) > 0:
    # Usually the first result is the most relevant
    result = data['organic_results'][0]
    paper_title = result.get('title', '')

    # Citation count is in inline_links.cited_by.total
    if 'inline_links' in result and 'cited_by' in result['inline_links']:
        num_citations = result['inline_links']['cited_by'].get('total', 0)

    print(f"Title: {paper_title}")
    print(f"Citations: {num_citations}")
else:
    print("No results found")
    exit(1)

# Create citation badge
badge_url = f"https://img.shields.io/badge/Citations-{num_citations}-blue?logo=googlescholar"
r = requests.get(badge_url)

if r.status_code != 200:
    print("Error downloading badge data")
    exit(1)

with open("citations.svg", "w") as f:
    f.write(r.text)

print(f"Badge saved to citations.svg")
