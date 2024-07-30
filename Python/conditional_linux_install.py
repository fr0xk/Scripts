import subprocess
import os

DISK = "/dev/sdX"
BOOT_PART = f"{DISK}1"
ROOT_PART = f"{DISK}2"
CHROOT_DIR = "/mnt"

def run_command(command):
    """Run a shell command and handle errors."""
    result = subprocess.run(command, shell=True, check=True)
    return result

# Partition disk
def partition_disk():
    run_command(f"parted {DISK} -- mklabel gpt")
    run_command(f"parted {DISK} -- mkpart primary fat32 1MiB 512MiB")
    run_command(f"parted {DISK} -- mkpart primary btrfs 512MiB 100%")
    run_command(f"parted {DISK} -- set 1 boot on")

def format_and_mount():
    run_command(f"mkfs.vfat -F 32 {BOOT_PART}")
    run_command(f"mkfs.btrfs -f {ROOT_PART}")

    run_command(f"mount {ROOT_PART} {CHROOT_DIR}")
    os.makedirs(f"{CHROOT_DIR}/boot", exist_ok=True)
    run_command(f"mount {BOOT_PART} {CHROOT_DIR}/boot")

def detect_distro():
    """Detect the distribution based on files in the chroot directory."""
    distros = {
        "/etc/arch-release": "arch",
        "/etc/gentoo-release": "gentoo",
        "/etc/debian_version": "debian",
        "/etc/alpine-release": "alpine"
    }
    for file, distro in distros.items():
        if os.path.exists(f"{CHROOT_DIR}{file}"):
            return distro
    return None

def arch_install():
    run_command(f"pacstrap {CHROOT_DIR} base linux linux-firmware")
    run_command(f"genfstab -U {CHROOT_DIR} >> {CHROOT_DIR}/etc/fstab")

    chroot_commands = """
    ln -sf /usr/share/zoneinfo/UTC /etc/localtime
    hwclock --systohc
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
    locale-gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    echo "archlinux" > /etc/hostname
    systemctl enable dhcpcd
    pacman -S --noconfirm grub
    grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=arch
    grub-mkconfig -o /boot/grub/grub.cfg
    """
    run_command(f"arch-chroot {CHROOT_DIR} /bin/bash -c '{chroot_commands}'")

def gentoo_install():
    # Create Btrfs subvolumes
    run_command(f"mount -o noatime,compress=zstd,space_cache,subvol=@root {ROOT_PART} {CHROOT_DIR}")
    os.makedirs(f"{CHROOT_DIR}/home", exist_ok=True)
    os.makedirs(f"{CHROOT_DIR}/.snapshots", exist_ok=True)
    run_command(f"mount -o noatime,compress=zstd,space_cache,subvol=@home {ROOT_PART} {CHROOT_DIR}/home")
    run_command(f"mount -o noatime,compress=zstd,space_cache,subvol=@snapshots {ROOT_PART} {CHROOT_DIR}/.snapshots")

    # Download and extract stage3 tarball
    STAGE3_URL = "http://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64/stage3-amd64-<DATE>.tar.xz"
    run_command(f"wget {STAGE3_URL} -O {CHROOT_DIR}/stage3.tar.xz")
    run_command(f"tar xpf {CHROOT_DIR}/stage3.tar.xz -C {CHROOT_DIR} --xattrs-include='*.*' --numeric-owner")

    # Copy DNS info
    run_command(f"cp -L /etc/resolv.conf {CHROOT_DIR}/etc/")

    # Mount necessary filesystems
    run_command(f"mount -t proc proc {CHROOT_DIR}/proc")
    run_command(f"mount --rbind /sys {CHROOT_DIR}/sys")
    run_command(f"mount --make-rslave {CHROOT_DIR}/sys")
    run_command(f"mount --rbind /dev {CHROOT_DIR}/dev")
    run_command(f"mount --make-rslave {CHROOT_DIR}/dev")

    # Chroot and configure
    chroot_commands = """
    source /etc/profile
    export PS1="(chroot) ${PS1}"
    echo 'COMMON_FLAGS="-O2 -pipe"' > /etc/portage/make.conf
    echo 'CFLAGS="${COMMON_FLAGS}"' >> /etc/portage/make.conf
    echo 'CXXFLAGS="${COMMON_FLAGS}"' >> /etc/portage/make.conf
    echo 'FCFLAGS="${COMMON_FLAGS}"' >> /etc/portage/make.conf
    echo 'FFLAGS="${COMMON_FLAGS}"' >> /etc/portage/make.conf
    echo 'USE="bindist btrfs"' >> /etc/portage/make.conf
    echo 'GENTOO_MIRRORS="http://distfiles.gentoo.org"' >> /etc/portage/make.conf
    echo 'GRUB_PLATFORMS="efi-64"' >> /etc/portage/make.conf
    emerge-webrsync
    emerge --sync
    emerge -uvDN @world
    echo "UTC" > /etc/timezone
    emerge --config sys-libs/timezone-data
    echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen
    locale-gen
    eselect locale set en_US.utf8
    env-update && source /etc/profile
    emerge sys-kernel/gentoo-sources
    emerge sys-kernel/genkernel
    genkernel all
    emerge sys-apps/util-linux sys-apps/busybox sys-fs/btrfs-progs
    echo "${ROOT_PART} / btrfs noatime,compress=zstd,space_cache,subvol=@root 0 0" > /etc/fstab
    echo "${ROOT_PART} /home btrfs noatime,compress=zstd,space_cache,subvol=@home 0 0" >> /etc/fstab
    echo "${ROOT_PART} /.snapshots btrfs noatime,compress=zstd,space_cache,subvol=@snapshots 0 0" >> /etc/fstab
    echo "${BOOT_PART} /boot vfat defaults 0 2" >> /etc/fstab
    echo "gentoo" > /etc/hostname
    echo "root:password" | chpasswd
    emerge sys-boot/grub:2
    grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=gentoo
    grub-mkconfig -o /boot/grub/grub.cfg
    emerge --noreplace net-misc/netifrc
    echo 'config_eth0="dhcp"' > /etc/conf.d/net
    ln -s /etc/init.d/net.lo /etc/init.d/net.eth0
    rc-update add net.eth0 default
    emerge net-misc/dhcpcd
    rc-update add dhcpcd default
    emerge net-wireless/iw net-wireless/wpa_supplicant
    rc-update add wpa_supplicant default
    cat <<EOL > /etc/wpa_supplicant/wpa_supplicant.conf
    ctrl_interface=/var/run/wpa_supplicant
    ctrl_interface_group=wheel
    update_config=1
    network={
        ssid="your_SSID"
        psk="your_password"
    }
    EOL
    echo 'wpa_supplicant_args="-c /etc/wpa_supplicant/wpa_supplicant.conf -D nl80211,wext -i wlan0"' > /etc/conf.d/wpa_supplicant
    ln -s /etc/init.d/net.lo /etc/init.d/net.wlan0
    rc-update add net.wlan0 default
    rc-update add sshd default
    rc-update add syslog-ng default
    rc-update add cronie default
    """
    run_command(f"chroot {CHROOT_DIR} /bin/bash -c '{chroot_commands}'")

def debian_install():
    run_command(f"debootstrap --arch amd64 bookworm {CHROOT_DIR} http://deb.debian.org/debian/")

    run_command(f"mount --bind /dev {CHROOT_DIR}/dev")
    run_command(f"mount --bind /proc {CHROOT_DIR}/proc")
    run_command(f"mount --bind /sys {CHROOT_DIR}/sys")

    chroot_commands = """
    ln -sf /usr/share/zoneinfo/UTC /etc/localtime
    dpkg-reconfigure -f noninteractive tzdata
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
    locale-gen
    echo "LANG=en_US.UTF-8" > /etc/default/locale
    echo "debian" > /etc/hostname
    apt-get install -y network-manager
    systemctl enable NetworkManager
    apt-get install -y grub-efi
    grub-install --target=x86_64-efi --efi-directory=/boot --boot
      grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=debian
    update-grub
    """
    run_command(f"chroot {CHROOT_DIR} /bin/bash -c '{chroot_commands}'")

def alpine_install():
    run_command(f"apk add --root {CHROOT_DIR} --initdb alpine-base")

    # Create fstab
    fstab_contents = f"""
{ROOT_PART} / btrfs noatime,compress=zstd,space_cache,subvol=@root 0 0
{ROOT_PART} /home btrfs noatime,compress=zstd,space_cache,subvol=@home 0 0
{ROOT_PART} /.snapshots btrfs noatime,compress=zstd,space_cache,subvol=@snapshots 0 0
{BOOT_PART} /boot vfat defaults 0 2
"""
    with open(f"{CHROOT_DIR}/etc/fstab", "w") as fstab_file:
        fstab_file.write(fstab_contents)

    chroot_commands = """
    ln -sf /usr/share/zoneinfo/UTC /etc/localtime
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/profile.d/locale.sh
    echo "alpine" > /etc/hostname
    rc-update add networking
    apk add --no-cache grub
    grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=alpine
    grub-mkconfig -o /boot/grub/grub.cfg
    """
    run_command(f"chroot {CHROOT_DIR} /bin/sh -c '{chroot_commands}'")

def cleanup():
    run_command(f"umount -l {CHROOT_DIR}/dev{/shm,/pts,}")
    run_command(f"umount -R {CHROOT_DIR}")

def main():
    partition_disk()
    format_and_mount()
    
    distro = detect_distro()
    
    if distro == "arch":
        arch_install()
    elif distro == "gentoo":
        gentoo_install()
    elif distro == "debian":
        debian_install()
    elif distro == "alpine":
        alpine_install()
    else:
        print("Unsupported distribution: {distro}")
        exit(1)
    
    cleanup()
    print("Installation complete. Reboot now.")

if __name__ == "__main__":
    main()
  
