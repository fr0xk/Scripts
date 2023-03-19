#!/bin/bash

# Check that script is running as root

if [[ $(id -u) -ne 0 ]]; then

    echo "This script must be run as root."

    exit 1

fi

# Check that required packages are installed

if ! dpkg -l lvm2 >/dev/null 2>&1; then

    echo "The lvm2 package is not installed. Please install it with 'sudo apt-get install lvm2' and run this script again."

    exit 1

fi

# Find available partitions on the system

partitions=($(lsblk -rno NAME,TYPE,MOUNTPOINT | grep '^/dev/' | grep -v '^/dev/loop' | awk '$2 == "part" {print $1}'))

# Check that there are available partitions

if [ ${#partitions[@]} -eq 0 ]; then

    echo "No partitions found on the system. Please create a partition and run this script again."

    exit 1

fi

# Display menu of available partitions

echo "Available partitions:"

for i in "${!partitions[@]}"; do

    echo "$((i+1))) ${partitions[$i]}"

done

# Prompt user to select partition

read -p "Enter the number of the partition to convert to a logical volume: " choice

selected_partition=${partitions[$((choice-1))]}

# Check that selected partition is not the root partition

if [[ $selected_partition == $(mount | awk '$3 == "/" {print $1}') ]]; then

    echo "Cannot convert root partition to logical volume."

    exit 1

fi

# Convert selected partition to a logical volume

lv_name=$(echo $selected_partition | awk -F '/' '{print $NF}')

lv_path=$(echo $selected_partition | sed "s/\/$lv_name$//")

lvcreate -n $lv_name -L +100%FREE $lv_path

# Take snapshot of entire logical volume

lv_path=$(echo $selected_partition | sed "s/$lv_name//")

lvcreate -s -n $lv_name-snap -L 1G $lv_path$lv_name

echo "Logical volume created and snapshot taken successfully."

# List all snapshots

echo "Available snapshots:"

lvs -a -o name,lv_time,lv_attr,origin $lv_path$lv_name

# Prompt user to restore snapshot

read -p "Would you like to restore a snapshot? (y/n) " choice

if [[ $choice == "y" ]]; then

    read -p "Enter the name of the snapshot to restore: " snapshot_name

    lvconvert --merge $lv_path$lv_name-snap

    echo "Snapshot $snapshot_name restored successfully."

fi

