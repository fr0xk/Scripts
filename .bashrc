# Only use color codes if output is to a terminal

if [ -t 1 ]; then

  # Set the prompt to display the current directory and username in a stylish way

  PS1='\[\e[32m\]\u@\h\[\e[34m\] \w \$\[\e[0m\] '

  # Set a nice color scheme for grep

  export GREP_OPTIONS='--color=auto'

  # Set a nice color scheme for less

  export LESS_TERMCAP_md=$'\e[1;38;5;74m' # begin bold

  export LESS_TERMCAP_mb=$'\e[1;31m'     # begin blinking

  export LESS_TERMCAP_me=$'\e[0m'         # end mode

  export LESS_TERMCAP_se=$'\e[0m'         # end standout-mode

  export LESS_TERMCAP_so=$'\e[38;5;246m'  # begin standout-mode - info box

  export LESS_TERMCAP_ue=$'\e[0m'         # end underline

  export LESS_TERMCAP_us=$'\e[4;38;5;146m' # begin underline - URL

  # Add some customization to ls command

  export LS_COLORS=$LS_COLORS:'di=0;34:' # set directory color to blue

fi

# Define some useful aliases

alias ll='ls -alF'

alias la='ls -A'

alias l='ls -CF'

# Enable colors for ls command

alias ls='ls --color=auto'

# Make cd more intuitive by automatically listing directory contents after changing directories

function cd() {

  builtin cd "$@" && ls -la

}

# Display an error message if any command fails

function check_error() {

  if [ "$?" -ne 0 ]; then

    echo -e "\033[31m[ERROR] Command failed!\033[0m"

  fi

}

trap { check_error; } ERR

