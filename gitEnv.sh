#!/bin/bash

function update_termux {
  echo "Updating and upgrading Termux..."
  pkg update -y && pkg upgrade -y
}

function install_encryption_tools {
  echo "Installing encryption tools..."
  pkg install -y gnupg openssh pinentry-curses
}

function set_up_gpg {
  echo "Setting up GPG configuration..."
  gpg --gen-key
}

function set_up_git {
  echo "Setting up Git configuration..."
  read -p "Enter your full name for Git: " name
  read -p "Enter your email address for Git: " email
  git config --global user.name "$name"
  git config --global user.email "$email"
  git config --global credential.helper store
}

function create_github_repo {
  echo "Creating test repository on GitHub..."
  read -p "Enter your GitHub username: " username
  read -p "Enter your GitHub personal access token: " token
  curl -u "$username:$token" https://api.github.com/user/repos -d '{"name":"test"}'
}

function set_up_ssh {
  echo "Setting up SSH connection..."
  read -p "Enter your email address for the SSH key: " ssh_email
  ssh-keygen -t rsa -b 4096 -C "$ssh_email"
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa
}

function display_ssh_keys {
  echo "Your private SSH key is:"
  cat ~/.ssh/id_rsa

  echo "Your public SSH key is:"
  cat ~/.ssh/id_rsa.pub
}

function set_up_gpg {
  echo "Setting up GPG configuration..."
  gpg --gen-key
}

function add_gpg_key {
  echo "Adding GPG key..."
  read -p "Enter the email address associated with your GPG key: " email
  read -p "Enter the name you want to associate with your GPG key: " name
  gpg --list-secret-keys --keyid-format LONG
  read -p "Enter the key ID for the GPG key you want to add: " key_id
  git config --global user.signingkey "$key_id"
  git config --global commit.gpgsign true
  echo "Your GPG key has been added and configured for Git."
}

function display_gpg_keys {
  echo "Your GPG key pairs are:"
  gpg --list-keys
  gpg --list-secret-keys
}

function test_ssh_connection {
  echo "Testing SSH connection to GitHub..."
  ssh -T git@github.com
}

# Perform setup steps
update_termux

# Install encryption tools and set up GPG
install_encryption_tools
set_up_gpg

# Set up Git and create test repository on GitHub
set_up_git
create_github_repo

# Set up SSH and display keys
set_up_ssh
display_ssh_keys

# Add and configure GPG key and display keys
add_gpg_key
display_gpg_keys

# Test SSH connection to GitHub
test_ssh_connection

echo "Setup complete."
