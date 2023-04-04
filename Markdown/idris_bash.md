# IDRIS influence in bash scripting 

In Idris, we would typically use types to define the structure of the data being manipulated, and functions to manipulate that data. We would also use algebraic data types to represent different variants of a value.

```bash
#!/bin/bash

# Check for root access

if [ $(id -u) -ne 0 ]; then

  echo "This script must be run as root"

  exit 1

fi

# Define package types

declare -A PackageTypes=(

  ["TermuxPackage"]="dpkg --get-selections | awk '{print \$1}'"

  ["PythonPackage"]="pip freeze | cut -d'=' -f1"

  ["AndroidApp"]="pm list packages -f | sed 's/.*=//'"

)

# List all packages and write backups

for pkgtype in "${!PackageTypes[@]}"; do

  ${PackageTypes[$pkgtype]} > "${pkgtype,,}_packages.txt"

done

# Prompt for reinstallation

read -p "Do you want to reinstall all packages? [y/n]: " choice

if [ "$choice" = "y" ]; then

  # Reinstall all packages

  for pkgtype in "${!PackageTypes[@]}"; do

    pkgs=$(cat "${pkgtype,,}_packages.txt")

    while read -r pkg; do

      case $pkgtype in

        "TermuxPackage") pkgmgr="pkg";;

        "PythonPackage") pkgmgr="pip";;

        "AndroidApp") pkgmgr="pm";;

      esac

      $pkgmgr install "$pkg"

    done <<< "$pkgs"

  done

else

  echo "No packages will be reinstalled"

fi
```
