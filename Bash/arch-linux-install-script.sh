#!/bin/bash
set -e

# Arch Linux Installation Script
# This script installs Arch Linux on an SSD with BTRFS root filesystem

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
mkdir -p /mnt/{home,boot,snapshots}
mount -o subvol=@home,compress=zstd /dev/sda2 /mnt/home
mount -o subvol=@snapshots,compress=zstd /dev/sda2 /mnt/snapshots
mount /dev/sda1 /mnt/boot

# Install base system
pacstrap /mnt base base-devel linux linux-firmware btrfs-progs vim

# Generate fstab
genfstab -U /mnt >> /mnt/etc/fstab

# Chroot and configure the system
arch-chroot /mnt /bin/bash << EOF
# Set timezone
ln -sf /usr/share/zoneinfo/UTC /etc/localtime
hwclock --systohc

# Set locale
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf

# Set hostname
echo "arch-system" > /etc/hostname

# Set root password
echo "Set root password:"
passwd

# Install and configure bootloader (GRUB)
pacman -S grub efibootmgr --noconfirm
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg

# Install additional packages for system recovery
pacman -S arch-install-scripts btrfs-progs --noconfirm

# Enable BTRFS snapshots in GRUB
sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet"/GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet rootflags=subvol=@"/' /etc/default/grub
grub-mkconfig -o /boot/grub/grub.cfg
EOF

echo "Arch Linux installation complete!"
