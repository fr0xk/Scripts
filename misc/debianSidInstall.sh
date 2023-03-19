#!/bin/bash

# Set variables
USERNAME='user'
VENV_NAME='env'
DESKTOP_ENVIRONMENT='lxqt'

# Prompt the user for the disk to use
echo "Enter the disk to use (e.g. /dev/sda):"
read DISK

# Check if script is being run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Partition the disk and create LVM volumes
printf "o\nn\np\n1\n\n\nw\n" | fdisk $DISK || { echo "Failed to partition disk"; exit 1; }
pvcreate ${DISK}1 || { echo "Failed to create physical volume"; exit 1; }
vgcreate $VG_NAME ${DISK}1 || { echo "Failed to create volume group"; exit 1; }
lvcreate -n $LV_ROOT_NAME -L 100%FREE $VG_NAME || { echo "Failed to create logical volume"; exit 1; }

# Format the partitions
mkfs.ext4 /dev/$VG_NAME/$LV_ROOT_NAME || { echo "Failed to format root partition"; exit 1; }
echo "/dev/$VG_NAME/$LV_ROOT_NAME / ext4 defaults 0 0" >> /etc/fstab || { echo "Failed to add root partition to fstab"; exit 1; }
mkswap ${DISK}1 || { echo "Failed to create swap partition"; exit 1; }
echo "${DISK}1 none swap sw 0 0" >> /etc/fstab || { echo "Failed to add swap partition to fstab"; exit 1; }
swapon ${DISK}1 || { echo "Failed to activate swap partition"; exit 1; }

# Mount the file systems
mount -a || { echo "Failed to mount file systems"; exit 1; }

# Install Debian Sid from minimal bootable drive
debootstrap sid /mnt http://deb.debian.org/debian || { echo "Failed to install Debian Sid"; exit 1; }

# Chroot into the new installation
chroot /mnt /bin/bash <<EOF || { echo "Failed to chroot into new installation"; exit 1; }

# Update the system
apt update || { echo "Failed to update system"; exit 1; }
apt upgrade -y || { echo "Failed to upgrade system"; exit 1; }

# Install the virtualenv package if it's not already installed
if ! command -v virtualenv >/dev/null 2>&1; then
apt install -y python3-virtualenv || { echo "Failed to install virtualenv"; exit 1; }
fi

# Create a virtual environment
su - $USERNAME <<VENVEOF
cd ~
virtualenv -p python3 $VENV_NAME || { echo "Failed to create virtual environment"; exit 1; }
VENVEOF

# Configure the bash prompt
echo "PS1='[\e[1;32m][\u@\h \W]\$[\e[0m] '" >> /home/$USERNAME/.bashrc || { echo "Failed to configure bash prompt"; exit 1; }

# Configure sound and video environment
apt install -y alsa-utils pulseaudio pavucontrol xorg xserver-xorg-video-all || { echo "Failed to install sound and video packages"; exit 1; }

# Install the desktop environment
apt install -y xfce4 || { echo "Failed to install desktop environment"; exit 1; }

# Clean up
apt autoremove -y
apt autoclean

#Create LVM backup
lvcreate -L 1G -s -n lv_backup /dev/vg0/lv_root || { echo "Failed to create LVM backup"; exit 1; }

echo "Installation successful!"
