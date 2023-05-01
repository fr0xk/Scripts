#!/bin/sh

# Check if the script is being run as root

is_root_user() {

  [ "$(id -u)" = "0" ]

}

# Install Node.js

install_nodejs() {

  echo "Node.js is not installed. Installing now..."

  curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -

  sudo apt-get install -y nodejs

}

# Install npm

install_npm() {

  echo "npm is not installed. Installing now..."

  sudo apt-get install -y npm

}

# Install build-essential

install_build_essential() {

  echo "build-essential is not installed. Installing now..."

  sudo apt-get install -y build-essential

}

# Install git

install_git() {

  echo "git is not installed. Installing now..."

  sudo apt-get install -y git

}

# Clone the Gunbot repository

clone_gunbot_repo() {

  if [ ! -d "BTCT" ]; then

    echo "Cloning the Gunbot repository..."

    git clone https://github.com/GuntharDeNiro/BTCT.git

  else

    echo "Gunbot repository already exists. Skipping clone."

  fi

}

# Install Gunbot dependencies

install_gunbot_dependencies() {

  echo "Installing Gunbot dependencies..."

  cd BTCT

  npm install --only=production

}

# Create config.js file

create_config_file() {

  if [ ! -f "config.js" ]; then

    echo "Creating a new config.js file..."

    cp config.js.example config.js

  else

    echo "config.js file already exists. Skipping creation."

  fi

}

# Start Gunbot

start_gunbot() {

  echo "Starting Gunbot..."

  nodejs gunthy.js

}

# Check for dependencies and install if necessary

install_dependencies() {

  is_dependency_installed() {

    command -v $1 >/dev/null 2>&1

  }

  if ! is_dependency_installed "nodejs"; then

    install_nodejs

  fi

  if ! is_dependency_installed "npm"; then

    install_npm

  fi

  if ! is_dependency_installed "build-essential"; then

    install_build_essential

  fi

  if ! is_dependency_installed "git"; then

    install_git

  fi

}

# Main function

main() {

  if ! is_root_user; then

    echo "This script must be run as root" 1>&2

    exit 1

  fi

  install_dependencies

  clone_gunbot_repo

  install_gunbot_dependencies

  create_config_file

  start_gunbot

}

# Call the main function

main

