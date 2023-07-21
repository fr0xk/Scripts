#!/bin/bash

# Clone the repository using HTTPS.
# Generate an SSH key pair.
ssh-keygen -t rsa -b 4096

# Add the public key to your GitHub account.
cat ~/.ssh/id_rsa.pub | ssh fr0xk@github.com 'cat >> ~/.ssh/authorized_keys'

# Start the SSH agent and add your private key to it.
eval "$(ssh-agent -s)"
ssh-add -k ~/.ssh/id_rsa

# Add the SSH key to your SSH config permanently.
echo "Host github.com
  IdentityFile ~/.ssh/id_rsa" >> ~/.ssh/config

