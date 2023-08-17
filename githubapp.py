# 테스트 8/17 
# 테스트 8/17 2

from pathlib import Path
import sys, os

import os.path
import pathlib
import json
from github import Github

# GIT HUB info
GIT_TOKEN='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'
OWNER='vmssupport'
REPO='TechDoc'

git = Github(GIT_TOKEN)
repo = git.get_repo(f"{OWNER}/{REPO}")

issue = repo.get_issue(26)

print(issue.repository.pulls_url)

branch = repo.get_branch('task-17')
print(branch.name)


'''
#create issue
issue = repo.create_issue(
        title="NID100", 
        body="this is the body of the issue"
)

# create branch
sb = repo.get_branch('master')
repo.create_git_ref(ref='refs/heads/' + issue.title, sha=sb.commit.sha)
'''


'''
issues = repo.get_issues()
for i in issues:
    print(i.body)
        

branches = repo.get_branches()
for b in branches:
    print(b.name)
    

commits = repo.get_commits()
for c in commits:
    print(c.sha)
    print(c.url)
    print(c.etag)
    print(c.html_url)    
    print(c.commit)
'''




        

