#!/bin/bash
set -e

# Debian Installation Script
# This script installs Debian on an SSD with BTRFS root filesystem using offline ISO method

# Ensure script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 
    exit 1
fi

# Partition the disk (assuming /dev/sda is the target SSD)
parted /dev/sda mklabel gpt
parted /dev/sda mkpart ESP fat32 1MiB 513MiB
parted /dev/sda set 1 boot on
parted /dev/sda mkpart primary btrfs 513MiB 100%

# Format partitions
mkfs.fat -F32 /dev/sda1
mkfs.btrfs /dev/sda2

# Mount the root partition
mount /dev/sda2 /mnt

# Create BTRFS subvolumes
btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home
btrfs subvolume create /mnt/@snapshots

# Unmount and remount with subvolumes
umount /mnt
mount -o subvol=@,compress=zstd /dev/sda2 /mnt
mkdir -p /mnt/{home,boot/efi,snapshots}
mount -o subvol=@home,compress=zstd /dev/sda2 /mnt/home
mount -o subvol=@snapshots,compress=zstd /dev/sda2 /mnt/snapshots
mount /dev/sda1 /mnt/boot/efi

# Assuming the Debian ISO is mounted at /cdrom
# Copy the contents of the ISO to the new system
cp -a /cdrom/. /mnt

# Prepare for chroot
mount --bind /dev /mnt/dev
mount --bind /dev/pts /mnt/dev/pts
mount --bind /proc /mnt/proc
mount --bind /sys /mnt/sys

# Chroot and configure the system
chroot /mnt /bin/bash << EOF

# Set up apt sources
cat > /etc/apt/sources.list << INNEREOF
deb http://deb.debian.org/debian bullseye main
deb-src http://deb.debian.org/debian bullseye main

deb http://security.debian.org/debian-security bullseye-security main
deb-src http://security.debian.org/debian-security bullseye-security main
INNEREOF

# Update and install necessary packages
apt update
apt install -y linux-image-amd64 grub-efi-amd64 btrfs-progs vim

# Set timezone
ln -sf /usr/share/zoneinfo/UTC /etc/localtime
dpkg-reconfigure -f noninteractive tzdata

# Set locale
sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" > /etc/default/locale

# Set hostname
echo "debian-system" > /etc/hostname

# Set root password
echo "Set root password:"
passwd

# Install and configure bootloader (GRUB)
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=DEBIAN
update-grub

# Enable BTRFS snapshots in GRUB
sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="quiet"/GRUB_CMDLINE_LINUX_DEFAULT="quiet rootflags=subvol=@"/' /etc/default/grub
update-grub

# Create a non-root user
adduser --gecos "" debian_user

# Give sudo privileges to the new user
apt install -y sudo
usermod -aG sudo debian_user

EOF

# Unmount all partitions
umount -R /mnt

echo "Debian installation complete! You can now reboot into your new system."
