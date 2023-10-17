#!/bin/bash

# **Dynamically get the username from the user.**
echo "Enter your GitHub username:"
read username

# Check if the SSH key pair already exists.
if [ -f ~/.ssh/id_rsa ]; then
  echo "SSH key pair already exists. Skipping generation."
else
  # Generate an SSH key pair.
  ssh-keygen -t rsa -b 4096

  # Show the public key to the user.
  echo "Your public key is:"
  cat ~/.ssh/id_rsa.pub
fi

# Add the public key to the user's GitHub account.
cat ~/.ssh/id_rsa.pub | ssh ${username}@github.com 'cat >> ~/.ssh/authorized_keys'

# Check if the SSH agent is running.
if ! pgrep ssh-agent > /dev/null; then
  # Start the SSH agent.
  eval "$(ssh-agent -s)"
fi

# Add the private key to the SSH agent.
ssh-add -k ~/.ssh/id_rsa

# Add the SSH key to the user's SSH config permanently.
echo "Host github.com
  IdentityFile ~/.ssh/id_rsa" > ~/.ssh/config

# Test the SSH connection.
ssh -T ${username}@github.com

# **End-user-friendly message.**
echo "You have successfully configured SSH authentication for GitHub. You can now clone repositories and push changes without having to enter your password."

