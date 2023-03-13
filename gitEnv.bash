#!/bin/bash

# Reset and clear everything in SSH and GPG

echo "Resetting and clearing SSH and GPG..."

rm -rf $HOME/.ssh/*

gpgconf --kill gpg-agent

gpgconf --kill dirmngr

gpgconf --kill scdaemon

gpgconf --kill gpg-connect-agent

gpgconf --kill all

gpg --list-keys --with-keygrip | grep Keygrip | cut -d ' ' -f 2 | xargs gpg-connect-agent "keyinfo --force-card-status /bye"

# Set up SSH authentication

echo "Setting up SSH authentication..."

ssh-keygen -t ed25519 -C "$GITHUB_USERNAME@github.com" -f $HOME/.ssh/id_ed25519_github -N ''

echo "Please copy and paste the following SSH key to your GitHub account:"

cat $HOME/.ssh/id_ed25519_github.pub

# Set up GPG authentication

echo "Setting up GPG authentication..."

gpg --batch --gen-key <<EOF

Key-Type: default

Subkey-Type: default

Name-Real: $GPG_NAME_REAL

Name-Comment: $GPG_NAME_COMMENT

Name-Email: $GPG_NAME_EMAIL

Expire-Date: 0

%no-protection

%commit

EOF

gpg_key_id=$(gpg --list-secret-keys --keyid-format LONG | grep -E "^sec" | awk '{print $2}' | cut -d '/' -f 2) # Get GPG key ID

echo "Please copy and paste the following GPG key to your GitHub account:"

gpg --armor --export $gpg_key_id

# Configure git to use SSH and GPG authentication

echo "Configuring git to use SSH and GPG authentication..."

git config --global user.name "$GITHUB_NAME"

git config --global user.email "$GITHUB_EMAIL"

git config --global user.signingkey $gpg_key_id

git config --global core.sshCommand "ssh -i $HOME/.ssh/id_ed25519_github"

# Clone the repository

echo "Cloning the repository..."

git clone git@github.com:$GITHUB_USERNAME/Scripts.git $HOME/Scripts

# Change to the repository directory

cd $HOME/Scripts

# Configure git to use the origin remote with SSH authentication

echo "Configuring git to use the origin remote with SSH authentication..."

git remote set-url origin git@github.com:$GITHUB_USERNAME/Scripts.git

