#!/bin/bash

# Update package manager and installed packages
pkg update
pkg upgrade

# Install basic tools
pkg install -y git bash-completion curl wget vim

# Install Powerline fonts
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd ..
rm -rf fonts

# Set Powerline font in Termux settings
termux-setup-storage
mkdir -p ~/.termux/font/
cp /data/data/com.termux/files/home/.local/share/fonts/DejaVuSansMono/* ~/.termux/font/
echo 'font = "DejaVuSansMono.ttf"' >> ~/.termux/termux.properties

# Set up a beautiful Bash prompt
echo 'function parse_git_branch {
  git branch 2> /dev/null | sed -e "/^[^*]/d" -e "s/* \(.*\)/\1/"
}
function git_dirty {
  [[ $(git status 2> /dev/null | tail -n1) != "nothing to commit, working tree clean" ]] && echo "*"
}
function set_prompt {
  local GREEN="\[\033[1;32m\]"
  local BLUE="\[\033[1;34m\]"
  local CYAN="\[\033[1;36m\]"
  local GRAY="\[\033[1;37m\]"
  local RED="\[\033[1;31m\]"
  local WHITE="\[\033[1;97m\]"
  local YELLOW="\[\033[1;33m\]"
  local RESET="\[\033[0m\]"
  local PS1=""
  PS1+="$BLUE┌──[$GRAY\u$BLUE@$GRAY\h$BLUE]──[$CYAN\w$BLUE]"
  PS1+="\$(parse_git_branch)\$(git_dirty)"
  PS1+="$BLUE\n└─>$RESET "
  export PS1
}
set_prompt' >> ~/.bashrc

# Add custom aliases
echo 'alias ll="ls -l"' >> ~/.bashrc
echo 'alias la="ls -a"' >> ~/.bashrc

# Set up Vim environment
echo 'syntax on
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent
set number
set background=dark
colorscheme dracula' > ~/.vimrc

# Install Dracula color scheme for Vim
git clone https://github.com/dracula/vim.git ~/.vim/pack/themes/start/dracula

# Reload shell
source ~/.bashrc
