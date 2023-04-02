# Check if output is to a terminal before using color codes

if [ -t 1 ]; then

  # Set the prompt to display the current directory and username in a stylish way

  PS1='\[$(tput setaf 2)\]\u@\h\[$(tput setaf 4)\] \w \$\[$(tput sgr0)\] '

  # Set a nice color scheme for grep

  alias grep='grep --color=auto'

  # Set a nice color scheme for less

  if command -v tput >/dev/null 2>&1 && command -v less >/dev/null 2>&1; then

    export LESS_TERMCAP_md="$(tput bold)$(tput setaf 74)" # begin bold

    export LESS_TERMCAP_mb="$(tput bold)$(tput setaf 1)"  # begin blinking

    export LESS_TERMCAP_me="$(tput sgr0)"               # end mode

    export LESS_TERMCAP_se="$(tput sgr0)"               # end standout-mode

    export LESS_TERMCAP_so="$(tput setaf 246)"           # begin standout-mode - info box

    export LESS_TERMCAP_ue="$(tput sgr0)"               # end underline

    export LESS_TERMCAP_us="$(tput smul)$(tput setaf 146)" # begin underline - URL

  fi

  # Add some customization to ls command

  if command -v dircolors >/dev/null 2>&1; then

    eval "$(dircolors -b)"

    export LS_COLORS=$LS_COLORS:'di=0;34:' # set directory color to blue

  fi

fi

# Define some useful aliases

alias ll='ls -alF'

alias la='ls -A'

alias l='ls -CF'

# Enable colors for ls command

if command -v ls >/dev/null 2>&1; then

  alias ls='ls --color=auto'

fi

# Make cd more intuitive by automatically listing directory contents after changing directories

cd() {

  command cd "$@" && ls -la

}

# Display an error message if any command fails

check_error() {

  if [ "$?" -ne 0 ]; then

    echo -e "\033[31m[ERROR] ${1:-Command failed!}\033[0m"

  fi

}

# Check if ssh is installed and set up
if [ -x "$(command -v ssh)" ] && [ -f ~/.ssh/id_rsa ]; then
  # Add ssh key to ssh-agent
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa
fi


trap 'check_error' ERR;

