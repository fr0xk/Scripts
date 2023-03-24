#!/bin/bash

# Define a function to get user input securely and validate it

get_input() {

    while [[ -z "$input" ]]; do

        prompt="$1"

        required="$2"

        read -r -s -p "$prompt" input

        echo

        if [[ -z "$input" && "$required" == "true" ]]; then

            echo "Input is required."

        fi

    done

    echo "$input"

}

# Get user input for Git username and email

git_username=$(get_input "Enter your Git username: " true)

git_email=$(get_input "Enter your Git email address: " true)

# Configure Git with the user's information

git config --global user.name "$git_username"

git config --global user.email "$git_email"

# Get user input for the new SSH key filename

ssh_key_filename=$(get_input "Enter the new SSH key filename (e.g. id_ed25519_github): " true)

# Rename the default SSH key to the new filename

mv ~/.ssh/id_rsa ~/.ssh/$ssh_key_filename

# Generate a new SSH key for GitHub

ssh-keygen -t ed25519 -C "$git_email" -f ~/.ssh/$ssh_key_filename -q -N ""

# Set secure permissions for the SSH key files

chmod 400 ~/.ssh/$ssh_key_filename

chmod 400 ~/.ssh/$ssh_key_filename.pub

# Add the SSH key to the SSH agent

eval "$(ssh-agent -s)"

ssh-add ~/.ssh/$ssh_key_filename

# Prompt the user to add the SSH key to their GitHub account

echo "Please add the following SSH key to your GitHub account:"

cat ~/.ssh/$ssh_key_filename.pub

# Get user input for the GitHub repository URL and local path

repo_url=$(get_input "Enter the GitHub repository URL (e.g. git@github.com:<username>/<repository>.git): " true)

repo_path=$(get_input "Enter the local path where you want to clone the repository (e.g. ~/my_repository): " true)

# Clone the GitHub repository

git clone $repo_url $repo_path

# Change into the repository directory

cd $repo_path

# Pull from the repository to ensure that the local copy is up-to-date

git pull

# Create a README.md file and commit it to the repository

echo "# My Project\n\nThis is my project." > README.md

git add README.md

git commit -m "Add README.md"

# Push the changes to the GitHub repository

git push

# Remove the SSH key from the SSH agent

ssh-add -D ~/.ssh/$ssh_key_filename

