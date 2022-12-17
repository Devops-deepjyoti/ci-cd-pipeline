from github import Github

# First create a Github instance:
# using an access token
g = Github("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")
# Then play with your Github objects:
for repo in g.get_user().get_repos('ci-cd-pipeline'):
    print(repo.name)

commit = repo.get_commit(sha="c1aed8f85fbcc69a7507057c326cc0f9edd046cc")
print(commit.commit.author.date)
print(commit.commit.committer.date)
