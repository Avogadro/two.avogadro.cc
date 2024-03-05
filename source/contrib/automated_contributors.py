import os
from github import Github
from github import Auth

# get access token from environment variable in github actions
access_token = os.environ.get("GITHUB_TOKEN")

if not access_token:
    raise ValueError("GITHUB_TOKEN environment variable not set")

auth = Auth.Token(access_token)
g = Github(auth=auth)

repositories = [
    "openchemistry/avogadrolibs",
    "openchemistry/avogadroapp",
    "openchemistry/fragments",
    "openchemistry/molecules",
    "openchemistry/crystals",
    "openchemistry/avogenerators",
    "openchemistry/avogadro-commands",
    "openchemistry/avogadro-cclib",
]

unique_contributors = set()

with open("contributors.md", "w") as contributors_file:
    for repo_name in repositories:
        repo = g.get_repo(repo_name)
        contributors = repo.get_contributors()

        for contributor in contributors:
            username = contributor.login

            if username not in unique_contributors:
                user = g.get_user(username)

                # check if the user has a full name and if so, use it else use username
                if user is not None and user.name is not None:
                    contributors_file.write(f"- [{user.name}]({user.html_url})\n")
                else:
                    contributors_file.write(f"- [{username}](https://github.com/{username})\n")
                unique_contributors.add(username)

print("Contributors have been updated in contributors.md")
