#!/bin/sh

LOGFILE="/tmp/install.log"
MAX_RETRIES=3
BACKUP_DIR="/tmp/backup"

log() {
    echo "$(date) $1" >> "$LOGFILE"
}

error_exit() {
    log "Error: $1"
    exit 1
}

run_command() {
    local command="$1"
    local error_message="$2"
    local retries=${3:-$MAX_RETRIES}
    local attempt=0
    while [ $attempt -lt $retries ]; do
        if eval "$command"; then
            return
        else
            attempt=$((attempt + 1))
            log "$error_message, attempt $attempt"
            sleep 2
        fi
    done
    error_exit "$error_message after $retries retries"
}

backup_configuration() {
    [ ! -d "$BACKUP_DIR" ] && mkdir -p "$BACKUP_DIR"
    for path in /etc/hostname /etc/locale.conf /etc/sysctl.conf; do
        [ -e "$path" ] && cp "$path" "$BACKUP_DIR" && log "Backed up $path to $BACKUP_DIR"
    done
}

prompt_user() {
    read -p "Enter the hostname: " hostname
    read -p "Enter the username: " username
    read -sp "Enter the password: " password
    echo
    read -p "Enter the distribution name: " distribution
    read -p "Enter the WiFi name: " wifi_name
    echo
    echo "$hostname $username $password $distribution $wifi_name"
}

detect_installation_method() {
    if [ -e /cdrom ]; then
        echo 'cdrom'
    elif [ -e /live/boot-dev ]; then
        echo 'usb'
    else
        echo 'network'
    fi
}

detect_devices() {
    usb_devices=$(lsblk -o NAME,TRAN | awk '/usb/ {print $1}')
    graphical_card=$(lspci | awk '/VGA/ {print $1}')
    hard_disk=$(lsblk -o NAME,TYPE | awk '/disk/ {print $1}')
    
    log "Detected USB devices: $usb_devices"
    log "Detected graphical card: $graphical_card"
    log "Detected hard disk: $hard_disk"
}

install_base_system() {
    local install_method="$1"
    local distribution="$2"
    case "$install_method" in
        cdrom|usb)
            method_command="debootstrap --arch amd64 $distribution /mnt http://archive.ubuntu.com/ubuntu/dists/$distribution/main/installer/cdrom/current/amd64/base.tar.gz"
            ;;
        network)
            method_command="debootstrap --arch amd64 $distribution /mnt http://archive.ubuntu.com/ubuntu/dists/$distribution/main/installer/netboot/amd64/"
            ;;
        *)
            error_exit "Unknown installation method: $install_method"
            ;;
    esac
    run_command "$method_command" "Failed to install base system"
}

configure_chroot() {
    local hostname="$1"
    local username="$2"
    local password="$3"
    local wifi_name="$4"
    
    chroot_commands=$(cat <<EOF
echo '$hostname' > /etc/hostname
ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
dpkg-reconfigure --frontend=noninteractive tzdata
echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen
locale-gen
echo 'LANG=en_US.UTF-8' > /etc/locale.conf
echo '$password' | passwd $username
usermod -aG sudo $username
apt-get update
apt-get install -y linux-headers-$(uname -r) linux-image-amd64 spl kmod zfsutils-linux zfs-dkms zfs-zed hostapd dnsmasq vim openssh-server grub-pc ssh curl wget nano git
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB --recheck /dev/sda
update-grub
echo 'net.ipv4.ip_forward=1' >> /etc/sysctl.conf
sysctl -p
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables-save > /etc/iptables.ipv4.nat
echo 'iptables-restore < /etc/iptables.ipv4.nat' >> /etc/rc.local
EOF
    )
    run_command "chroot /mnt /bin/sh -c '$chroot_commands'" "Failed to configure chroot environment"
}

create_zfs_pool_and_datasets() {
    zfs_commands="\
zpool create -f -o ashift=12 -O compression=lz4 -O acltype=posixacl -O xattr=sa -O relatime=on -O mountpoint=/ -R /mnt rpool /dev/sda3
zfs create rpool/ROOT/debian
zfs create rpool/HOME"
    
    echo "$zfs_commands" | while IFS= read -r command; do
        run_command "$command" "Failed to execute ZFS command: $command"
    done
}

mount_filesystem() {
    run_command "mount /mnt/rpool/ROOT/debian /mnt" "Failed to mount root filesystem"
}

set_permissions() {
    run_command "chown -R root:root /mnt" "Failed to set permissions"
}

unmount_filesystems() {
    run_command "umount /mnt/dev /mnt/proc /mnt/sys" "Failed to unmount chroot filesystems"
    run_command "umount /mnt" "Failed to unmount /mnt"
}

reboot_system() {
    log "Rebooting system"
    run_command "reboot" "Failed to reboot system"
}

configure_systemd() {
    log "Configuring systemd job timeout"
    run_command "mkdir -p /etc/systemd/system.conf.d" "Failed to create systemd configuration directory"
    run_command "echo -e '[Manager]\nDefaultTimeoutStartSec=5s' > /etc/systemd/system.conf.d/override.conf" "Failed to write systemd configuration"
    run_command "systemctl daemon-reload" "Failed to reload systemd daemon"
}

main() {
    backup_configuration
    IFS=' ' read -r hostname username password distribution wifi_name < <(prompt_user)
    install_method=$(detect_installation_method)
    detect_devices
    install_base_system "$install_method" "$distribution"
    configure_chroot "$hostname" "$username" "$password" "$wifi_name"
    create_zfs_pool_and_datasets
    mount_filesystem
    set_permissions
    unmount_filesystems
    reboot_system
    configure_systemd
}

main
