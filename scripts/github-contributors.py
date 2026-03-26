#!/usr/bin/env python

import os
import sys

from github import Auth, Github

token = os.environ.get("GITHUB_TOKEN")
if not token:
    print("Error: GITHUB_TOKEN environment variable is required.", file=sys.stderr)
    sys.exit(1)

g = Github(auth=Auth.Token(token))

REPOS = [
    "cryos/avogadro",
    "openchemistry/avogadrolibs",
    "openchemistry/avogadroapp",
    "openchemistry/fragments",
    "openchemistry/molecules",
    "openchemistry/crystals",
    "openchemistry/avogenerators",
    "openchemistry/chemicaljson",
    "avogadro/two.avogadro.cc",
    "avogadro/manual",
]

# Known login -> display name overrides
NAME_OVERRIDES = {
    "serk12": "Marc Masó",
    "badarsh2": "Adarsh Balasubramanian",
    "taylorcornell": "Taylor Cornell",
    "weblate": "Weblate",
}

# Collect unique contributors by login across all repos
contributors = {}
for repo_name in REPOS:
    for contributor in g.get_repo(repo_name).get_contributors():
        login = contributor.login.lower()
        if "bot" not in login and login not in contributors:
            contributors[login] = contributor

# Resolve display names
names = []
for login, contributor in contributors.items():
    if login in NAME_OVERRIDES:
        names.append(NAME_OVERRIDES[login])
    elif contributor.name and "bot" not in contributor.name:
        names.append(contributor.name)
    else:
        names.append(contributor.login)

# Sort by last name
names.sort(key=lambda x: x.split()[-1].lower())

output = "\n".join(f"- {name}" for name in names) + "\n"

# Write to file if path given, otherwise print to stdout
if len(sys.argv) > 1:
    with open(sys.argv[1], "w") as f:
        f.write(output)
    print(f"Wrote {len(names)} contributors to {sys.argv[1]}")
else:
    print(output, end="")
