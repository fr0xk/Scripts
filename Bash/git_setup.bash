#!/bin/bash

# Check if SSH is installed and set up
if [ -z "$(which ssh)" ]; then
  echo "SSH is not installed. Please install and set it up before running this script."
  exit 1
fi

# Check if GPG is installed and set up
if [ -z "$(which gpg)" ]; then
  echo "GPG is not installed. Please install and set it up before running this script."
  exit 1
fi

# Set user identity for Git
echo "Please enter your email address for Git:"
read git_email
echo "Please enter your name for Git:"
read git_name
git config --global user.email "$git_email"
git config --global user.name "$git_name"

# Set up SSH authentication
if [ -f "$HOME/.ssh/id_rsa" ]; then
  echo "SSH key already exists. Skipping SSH key generation."
else
  echo "Generating new SSH key..."
  ssh-keygen -t rsa -b 4096 -C "$git_email"
fi

echo "Adding SSH key to SSH agent..."
eval "$(ssh-agent -s)"
ssh-add "$HOME/.ssh/id_rsa"

# Set up GPG authentication
echo "Exporting GPG key..."
gpg --armor --export "$git_email" > "$HOME/gpgkey.txt"

echo "Adding GPG key to Git..."
git config --global user.signingkey "$(gpg --list-secret-keys --keyid-format LONG | awk '$1 == "sec:" {print $2}' | cut -d '/' -f 2)"
git config --global commit.gpgsign true

# Clone a test repository to verify setup
echo "Cloning test repository to verify setup..."
git clone git@github.com:<username>/<repository>.git
cd <repository>
echo "Hello, world!" > hello.txt
git add hello.txt
git commit -m "Test commit"
git push

echo "Setup complete."

