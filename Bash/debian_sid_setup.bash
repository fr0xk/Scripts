#!/bin/bash

set -e  # Exit on error

# Check for root privileges

if [[ $EUID -ne 0 ]]; then

   echo "This script must be run as root" 

   exit 1

fi

# Configure variables

HOSTNAME="debian-sid"

USERNAME="user"

TIMEZONE="India/Kolkata"

LANG="en_US.UTF-8"

# Verify internet connection

ping -q -w 1 -c 1 google.com &>/dev/null || { echo "No internet connection detected. Aborting."; exit 1; }

# Update package repositories

apt update

# Install necessary packages

apt install -y debootstrap btrfs-progs grub-pc

# Create the chroot environment

debootstrap --variant=buildd --arch amd64 sid /mnt http://deb.debian.org/debian/

# Mount necessary filesystems

mount -t proc proc /mnt/proc

mount -t sysfs sys /mnt/sys

mount --bind /dev /mnt/dev

mount --bind /dev/pts /mnt/dev/pts

# Configure the chroot environment

chroot /mnt /bin/bash <<EOF

echo "$HOSTNAME" > /etc/hostname

echo "Setting root password..."

passwd root

ln -sf /usr/share/zoneinfo/$TIMEZONE /etc/localtime

echo "LANG=$LANG" > /etc/default/locale

locale-gen

echo "$LANG UTF-8" > /etc/locale.gen

locale-gen

echo "Setting user password..."

passwd $USERNAME

useradd -m -s /bin/bash $USERNAME

EOF

# Install desktop environment and btrfs tools

chroot /mnt /bin/bash -c "apt install -y xfce4 btrfs-progs"

# Create btrfs subvolumes and take snapshot

chroot /mnt /bin/bash -c "btrfs subvolume create /root && btrfs subvolume create /home && btrfs subvolume snapshot / /root/snapshot-latest && btrfs subvolume snapshot /home /root/home-snapshot-latest"

# List backed up snapshots and ask user if they want to restore one

chroot /mnt /bin/bash -c "echo 'List of backed up snapshots:'

btrfs subvolume list /root

echo ''

echo 'Would you like to restore a snapshot? [y/n]'

read restore

if [ \"\$restore\" == \"y\" ]; then

    echo 'Enter the snapshot ID:'

    read id

    btrfs subvolume delete / && btrfs subvolume snapshot /root/\$id / && mount -a

    echo 'Snapshot restored successfully.'

else

    echo 'Exiting.'

    read

fi

"

# Unmount filesystems

umount /mnt/proc

umount /mnt/sys

umount /mnt/dev/pts

umount /mnt/dev

umount /mnt

# Generate grub configuration

cat <<EOF > /mnt/boot/grub/grub.cfg

menuentry "Debian Sid" {

    set root=(hd0,1)

    linux /vmlinuz root=/dev/sda1 subvol=/root

    initrd /initrd.img

}

EOF

echo "Installation complete. Reboot to boot into the new system."

