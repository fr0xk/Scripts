#!/bin/ash
set -e

# Alpine Linux Installation Script (musl edition)
# This script installs Alpine Linux on an SSD with BTRFS root filesystem using offline installer

# Ensure script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 
    exit 1
fi

# Set variables
DISK="/dev/sda"
BOOT_PART="${DISK}1"
ROOT_PART="${DISK}2"

# Partition the disk
fdisk "$DISK" << EOF
g
n
1

+512M
t
1
n
2


w
EOF

# Format partitions
mkfs.vfat -F32 "$BOOT_PART"
mkfs.btrfs -f "$ROOT_PART"

# Mount the root partition
mount "$ROOT_PART" /mnt

# Create BTRFS subvolumes
btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home
btrfs subvolume create /mnt/@snapshots

# Unmount and remount with subvolumes
umount /mnt
mount -o subvol=@,compress=zstd "$ROOT_PART" /mnt
mkdir -p /mnt/{home,boot,snapshots}
mount -o subvol=@home,compress=zstd "$ROOT_PART" /mnt/home
mount -o subvol=@snapshots,compress=zstd "$ROOT_PART" /mnt/snapshots
mount "$BOOT_PART" /mnt/boot

# Install base system
apk --root=/mnt add alpine-base linux-lts vim btrfs-progs syslinux grub grub-efi efibootmgr

# Generate fstab
cat > /mnt/etc/fstab << EOF
$ROOT_PART / btrfs subvol=@,compress=zstd 0 1
$ROOT_PART /home btrfs subvol=@home,compress=zstd 0 2
$ROOT_PART /snapshots btrfs subvol=@snapshots,compress=zstd 0 2
$BOOT_PART /boot vfat defaults 0 2
EOF

# Chroot and configure the system
chroot /mnt /bin/ash << EOF

# Set timezone
setup-timezone -z UTC

# Set hostname
echo "alpine-system" > /etc/hostname

# Set root password
echo "Set root password:"
passwd

# Configure network
cat > /etc/network/interfaces << INNEREOF
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp
INNEREOF

# Enable services
rc-update add networking boot
rc-update add bootmisc boot
rc-update add hostname boot

# Install and configure bootloader (GRUB)
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=ALPINE
grub-mkconfig -o /boot/grub/grub.cfg

# Enable BTRFS snapshots in GRUB
sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="quiet"/GRUB_CMDLINE_LINUX_DEFAULT="quiet rootflags=subvol=@"/' /etc/default/grub
grub-mkconfig -o /boot/grub/grub.cfg

# Create a non-root user
adduser -D alpine_user
echo "Set password for alpine_user:"
passwd alpine_user

# Give sudo privileges to the new user
apk add sudo
echo "alpine_user ALL=(ALL) ALL" > /etc/sudoers.d/alpine_user

EOF

# Unmount all partitions
umount -R /mnt

echo "Alpine Linux installation complete! You can now reboot into your new system."
