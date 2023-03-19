#!/bin/bash

echo "Btrfs Filesystem Management Script"

echo "Available Btrfs filesystems:";lsblk -f|grep -e btrfs|awk '{print $1,$2}';read -p "Enter the device or mount point for the filesystem (e.g. /dev/sda1 or /mnt/btrfs): " DEVICE_OR_MOUNT_POINT

[ ! -e "$DEVICE_OR_MOUNT_POINT" ] && { echo "$DEVICE_OR_MOUNT_POINT is not a valid device or mount point"; exit 1; }

command -v mkfs.btrfs >/dev/null || { echo "Btrfs tools are not installed"; exit 1; }

! mountpoint -q "$DEVICE_OR_MOUNT_POINT" && { read -p "Do you want to create a new Btrfs filesystem? (y/n) " CREATE_NEW; [ "$CREATE_NEW" != "y" ] && exit 1; echo "Creating new Btrfs filesystem on $DEVICE_OR_MOUNT_POINT"; mkfs.btrfs -f "$DEVICE_OR_MOUNT_POINT"; echo "Filesystem created"; }

read -p "Enter the subvolume to use (e.g. /): " SUBVOLUME

! btrfs subvolume list "$DEVICE_OR_MOUNT_POINT"|grep -q " path $SUBVOLUME$" && { read -p "Do you want to create the subvolume? (y/n) " CREATE_NEW; [ "$CREATE_NEW" != "y" ] && exit 1; echo "Creating subvolume $SUBVOLUME in Btrfs filesystem mounted at $DEVICE_OR_MOUNT_POINT"; btrfs subvolume create "$DEVICE_OR_MOUNT_POINT/$SUBVOLUME"; echo "Subvolume created"; }

echo "Choose an action to take:"

echo "1. Take a snapshot"

echo "2. List snapshots"

echo "3. Roll back to snapshot"

read -p "Enter the number of the action to take: " ACTION

case $ACTION in

    1)

        read -p "Enter a name for the snapshot: " SNAPSHOT_NAME

        btrfs subvolume snapshot "$DEVICE_OR_MOUNT_POINT/$SUBVOLUME" "$DEVICE_OR_MOUNT_POINT/$SUBVOLUME\_$SNAPSHOT_NAME"

        echo "Snapshot taken"

        ;;

    2)

        echo "Snapshots of subvolume $SUBVOLUME in Btrfs filesystem mounted at $DEVICE_OR_MOUNT_POINT:"

        btrfs subvolume list -s "$DEVICE_OR_MOUNT_POINT" | grep -e "^ID" -e " path $SUBVOLUME/" | sed 's/^ID \([0-9]*\).* path \(.*\)/\1 \2/g'

        ;;

    3)

        echo "Snapshots of subvolume $SUBVOLUME in Btrfs filesystem mounted at $DEVICE_OR_MOUNT_POINT:"

        btrfs subvolume list -s "$DEVICE_OR_MOUNT_POINT" | grep -e "^ID" -e " path $SUBVOLUME/" | sed 's/^ID \([0-9]*\).* path \(.*\)/\1 \2/g'

        read -p "Enter the ID of the snapshot to roll back to: " SNAPSHOT_ID

        btrfs subvolume set-default $SNAPSHOT_ID "$DEVICE_OR_MOUNT_POINT/$SUBVOLUME"

        echo "Rolled back to snapshot with ID $SNAPSHOT_ID"

        ;;

    *)

        echo "Invalid action number"

        exit 1

        ;;

esac

