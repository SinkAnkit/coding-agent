"""GitHub integration for PR creation and issue management."""
import os
from typing import Optional
from github import Github, GithubException

class GitHubManager:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("GITHUB_TOKEN not found in environment")
        
        self.client = Github(self.token)
        self.repo_owner = os.getenv("GITHUB_REPO_OWNER")
        self.repo_name = os.getenv("GITHUB_REPO_NAME")
    
    def get_repo(self, owner: Optional[str] = None, name: Optional[str] = None):
        """Get repository object."""
        owner = owner or self.repo_owner
        name = name or self.repo_name
        return self.client.get_repo(f"{owner}/{name}")
    
    def get_issue(self, issue_number: int, owner: Optional[str] = None, name: Optional[str] = None):
        """Get issue by number."""
        repo = self.get_repo(owner, name)
        return repo.get_issue(issue_number)
    
    def create_pr(self, title: str, body: str, head_branch: str, base_branch: str = "main",
                  owner: Optional[str] = None, name: Optional[str] = None):
        """Create a pull request."""
        repo = self.get_repo(owner, name)
        try:
            pr = repo.create_pull(
                title=title,
                body=body,
                head=head_branch,
                base=base_branch
            )
            return pr
        except GithubException as e:
            raise Exception(f"Failed to create PR: {e.data.get('message', str(e))}")
    
    def create_branch(self, branch_name: str, from_branch: str = "main",
                      owner: Optional[str] = None, name: Optional[str] = None):
        """Create a new branch."""
        repo = self.get_repo(owner, name)
        source = repo.get_branch(from_branch)
        repo.create_git_ref(f"refs/heads/{branch_name}", source.commit.sha)
    
    def update_file(self, file_path: str, content: str, message: str, branch: str,
                    owner: Optional[str] = None, name: Optional[str] = None):
        """Update or create a file in repository."""
        repo = self.get_repo(owner, name)
        try:
            # Try to get existing file
            file = repo.get_contents(file_path, ref=branch)
            repo.update_file(file_path, message, content, file.sha, branch=branch)
        except GithubException:
            # File doesn't exist, create it
            repo.create_file(file_path, message, content, branch=branch)
