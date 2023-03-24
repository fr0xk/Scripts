#!/bin/bash

function backup_system {

  options=( "--one-file-system" "--xattrs" "--acls" "--selinux" "--exclude=/dev" "--exclude=/proc" "--exclude=/sys" "--exclude=/tmp" )

  (( $compress )) && options+=( "--gzip" )

  [[ -n $exclude ]] && options+=( "--exclude=$exclude" )

  sudo mount -o remount,ro /

  sudo tar "${options[@]}" -cpf "${destination}/system_backup_$(date +%Y%m%d%H%M%S).tar" /

  sudo mount -o remount,rw /

  echo "Backup created successfully in $destination"

}

function restore_system {

  read -p "Enter the full path to the backup file: " backup_file

  [[ ! -f $backup_file ]] && echo "Backup file not found!" && exit 1

  sudo mount -o remount,rw /

  sudo tar --numeric-owner --same-owner --xattrs --acls --selinux -xpf "$backup_file" -C /

  sudo mount -o remount,ro /

}

function menu {

  PS3="Please enter your choice: "

  select option in "Backup system" "Restore system" "Quit"; do

    case $option in

      "Backup system")

        read -p "Enter backup destination directory: " destination

        read -p "Do you want to compress the backup? (y/n): " compress

        read -p "Enter any files/directories to exclude (optional): " exclude

        sudo mount -o remount,rw /

        backup_system

        sudo mount -o remount,ro /

        break;;

      "Restore system")

        restore_system

        break;;

      "Quit")

        break;;

      *) echo "Invalid option. Try again.";;

    esac

  done

}

menu

