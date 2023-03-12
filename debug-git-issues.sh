#!/bin/sh

REPO_PATH=/path/to/your/repo

cd "$REPO_PATH" || exit 1

check_connection() { git ls-remote --exit-code >/dev/null 2>&1 || { echo "Failed to connect to remote repository." ; exit 1; } }

fetch_repository() { git fetch --all --tags; }

reset_repository() { git reset --hard "origin/$(git rev-parse --abbrev-ref HEAD)"; }

clean_repository() { git clean -dfx; }

pull_repository() { git pull; }

check_conflicts() {

  [ -n "$(git status --porcelain | grep "^UU")" ] && {

    mkdir -p backup || exit 1

    git diff --name-only --diff-filter=U | xargs -I '{}' cp --parents '{}' backup/

    force_reset_repository

  }

}

force_reset_repository() {

  git reset --hard "origin/$(git rev-parse --abbrev-ref HEAD)" && git clean -dfx && git pull

}

check_unstaged_changes() { [ -n "$(git status --porcelain)" ] && { echo "There are unstaged changes. Please commit or stash them." ; exit 1; } }

check_uncommitted_changes() { [ -n "$(git log --branches --not --remotes)" ] && { echo "There are uncommitted changes. Please commit or stash them." ; exit 1; } }

check_untracked_files() { [ -n "$(git ls-files --others --exclude-standard)" ] && { echo "There are untracked files. Please add or ignore them." ; exit 1; } }

check_connection

fetch_repository

reset_repository

clean_repository

pull_repository

check_conflicts

check_unstaged_changes

check_uncommitted_changes

check_untracked_files

echo "Git repository is up-to-date and clean."

