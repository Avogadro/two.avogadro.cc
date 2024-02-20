from github import Github
from github import Auth

access_token = "YOUR_ACCESS_TOKEN"

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
    "cryos/avogadro",
]

unique_contributors = set()

with open("contributors.md", "w") as contributors_file:
    for repo_name in repositories:
        repo = g.get_repo(repo_name)
        contributors = repo.get_contributors()

        for contributor in contributors:
            username = contributor.login
            unique_contributors.add(username)
            contributors_file.write(f"- {username}\n")

sorted_contributors = sorted(unique_contributors)

with open("credits.md", "r") as credits_file:
    credits_content = credits_file.read()

updated_credits_content = credits_content.replace(
    "```{include} contributors.md```",
    f"```{{include}} contributors.md\n\n" + "\n".join(sorted_contributors) + "\n```"
)

with open("credits.md", "w") as credits_file:
    credits_file.write(updated_credits_content)

print("Contributors have been updated in contributors.md and credits.md.")
