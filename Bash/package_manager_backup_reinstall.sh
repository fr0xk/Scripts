#!/bin/bash

# Identify package manager
if [ -f /etc/apt/sources.list ]; then
  package_manager="apt"
elif [ -d /etc/yum.repos.d/ ]; then
  package_manager="yum"
elif [ -f /etc/pacman.conf ]; then
  package_manager="pacman"
elif [ -f /etc/portage/make.conf ]; then
  package_manager="portage"
elif [ -f /usr/local/etc/pkg/repos/ ]; then
  package_manager="pkg"
else
  echo "Unsupported package manager"
  exit 1
fi

# Check for sudo privileges
if [ "$EUID" -ne 0 ]; then
  echo "This script requires superuser privileges. Please run with sudo."
  exit 1
fi

# Backup function
backup_packages() {
  case $package_manager in
    apt)
      dpkg --get-selections | awk '{print $1}' > package_list.txt
      ;;
    yum|dnf)
      yum list installed | awk 'NR>1 {print $1}' > package_list.txt
      ;;
    pacman)
      pacman -Q | awk '{print $1}' > package_list.txt
      ;;
    portage)
      # Portage backup with world file
      equery list '*' > package_list.txt
      ;;
    pkg)
      pkg info | awk '{print $1}' > package_list.txt
      ;;
  esac
}

# Reinstall function
reinstall_packages() {
  if [ ! -f package_list.txt ]; then
    echo "Backup file not found. Run backup_packages first."
    exit 1
  fi

  # Validate package list
  if grep -q '^$' package_list.txt || grep -q '[^a-zA-Z0-9\-_]' package_list.txt; then
    echo "Error: Invalid package name found in list. Backup might be corrupted."
    exit 1
  fi

  case $package_manager in
    apt)
      if sudo apt install $(cat package_list.txt) &> /dev/null; then
        echo "Packages reinstalled successfully."
      else
        echo "Error: Failed to reinstall packages using apt. Check the system logs for details."
      fi
      ;;
    yum|dnf)
      if sudo dnf install $(cat package_list.txt) &> /dev/null; then
        echo "Packages reinstalled successfully."
      else
        echo "Error: Failed to reinstall packages using dnf. Check the system logs for details."
      fi
      ;;
    pacman)
      sudo pacman -S --needed $(cat package_list.txt)
      ;;
    portage)
      sudo emerge -av $(cat package_list.txt)
      ;;
    pkg)
      sudo pkg install $(cat package_list.txt)
      ;;
  esac
}

# Usage message
echo "This script can backup and reinstall packages."
echo "Usage:"
echo "  backup_packages: Creates a list of installed packages (package_list.txt)"
echo "  reinstall_packages: Reinstalls packages from the backup file"
echo "** Note: Portage reinstall using package_list.txt is not recommended."
