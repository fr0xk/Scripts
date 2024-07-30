import subprocess
import os

DISK = "/dev/sdX"
BOOT_PART = f"{DISK}1"
ROOT_PART = f"{DISK}2"
CHROOT_DIR = "/mnt"

run_command = lambda command: subprocess.run(command, shell=True, check=True)

partition_disk = lambda: list(map(run_command, [
    f"parted {DISK} -- mklabel gpt",
    f"parted {DISK} -- mkpart primary fat32 1MiB 512MiB",
    f"parted {DISK} -- mkpart primary btrfs 512MiB 100%",
    f"parted {DISK} -- set 1 boot on"
]))

format_and_mount = lambda: list(map(run_command, [
    f"mkfs.vfat -F 32 {BOOT_PART}",
    f"mkfs.btrfs -f {ROOT_PART}",
    f"mount {ROOT_PART} {CHROOT_DIR}",
    f"mkdir -p {CHROOT_DIR}/boot",
    f"mount {BOOT_PART} {CHROOT_DIR}/boot"
]))

detect_distro = lambda: next(
    (distro for file, distro in {
        "/etc/arch-release": "arch",
        "/etc/gentoo-release": "gentoo",
        "/etc/debian_version": "debian",
        "/etc/alpine-release": "alpine"
    }.items() if os.path.exists(f"{CHROOT_DIR}{file}")), None
)

arch_install = lambda: run_command(f"arch-chroot {CHROOT_DIR} /bin/bash -c '"
    "ln -sf /usr/share/zoneinfo/UTC /etc/localtime && "
    "hwclock --systohc && "
    "echo \"en_US.UTF-8 UTF-8\" > /etc/locale.gen && "
    "locale-gen && "
    "echo \"LANG=en_US.UTF-8\" > /etc/locale.conf && "
    "echo \"archlinux\" > /etc/hostname && "
    "systemctl enable dhcpcd && "
    "pacman -S --noconfirm grub && "
    "grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=arch && "
    "grub-mkconfig -o /boot/grub/grub.cfg'")

gentoo_install = lambda: list(map(run_command, [
    f"mount -o noatime,compress=zstd,space_cache,subvol=@root {ROOT_PART} {CHROOT_DIR}",
    f"mkdir -p {CHROOT_DIR}/home",
    f"mkdir -p {CHROOT_DIR}/.snapshots",
    f"mount -o noatime,compress=zstd,space_cache,subvol=@home {ROOT_PART} {CHROOT_DIR}/home",
    f"mount -o noatime,compress=zstd,space_cache,subvol=@snapshots {ROOT_PART} {CHROOT_DIR}/.snapshots",
    f"wget http://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64/stage3-amd64-<DATE>.tar.xz -O {CHROOT_DIR}/stage3.tar.xz",
    f"tar xpf {CHROOT_DIR}/stage3.tar.xz -C {CHROOT_DIR} --xattrs-include='*.*' --numeric-owner",
    f"cp -L /etc/resolv.conf {CHROOT_DIR}/etc/",
    f"mount -t proc proc {CHROOT_DIR}/proc",
    f"mount --rbind /sys {CHROOT_DIR}/sys",
    f"mount --make-rslave {CHROOT_DIR}/sys",
    f"mount --rbind /dev {CHROOT_DIR}/dev",
    f"mount --make-rslave {CHROOT_DIR}/dev"
]) + [run_command(f"chroot {CHROOT_DIR} /bin/bash -c '"
    "source /etc/profile && "
    "export PS1=\"(chroot) ${PS1}\" && "
    "echo 'COMMON_FLAGS=\"-O2 -pipe\"' > /etc/portage/make.conf && "
    "echo 'CFLAGS=\"${COMMON_FLAGS}\"' >> /etc/portage/make.conf && "
    "echo 'CXXFLAGS=\"${COMMON_FLAGS}\"' >> /etc/portage/make.conf && "
    "echo 'FCFLAGS=\"${COMMON_FLAGS}\"' >> /etc/portage/make.conf && "
    "echo 'FFLAGS=\"${COMMON_FLAGS}\"' >> /etc/portage/make.conf && "
    "echo 'USE=\"bindist btrfs\"' >> /etc/portage/make.conf && "
    "echo 'GENTOO_MIRRORS=\"http://distfiles.gentoo.org\"' >> /etc/portage/make.conf && "
    "echo 'GRUB_PLATFORMS=\"efi-64\"' >> /etc/portage/make.conf && "
    "emerge-webrsync && "
    "emerge --sync && "
    "emerge -uvDN @world && "
    "echo \"UTC\" > /etc/timezone && "
    "emerge --config sys-libs/timezone-data && "
    "echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen && "
    "locale-gen && "
    "eselect locale set en_US.utf8 && "
    "env-update && source /etc/profile && "
    "emerge sys-kernel/gentoo-sources && "
    "emerge sys-kernel/genkernel && "
    "genkernel all && "
    "emerge sys-apps/util-linux sys-apps/busybox sys-fs/btrfs-progs && "
    "echo \"{ROOT_PART} / btrfs noatime,compress=zstd,space_cache,subvol=@root 0 0\" > /etc/fstab && "
    "echo \"{ROOT_PART} /home btrfs noatime,compress=zstd,space_cache,subvol=@home 0 0\" >> /etc/fstab && "
    "echo \"{ROOT_PART} /.snapshots btrfs noatime,compress=zstd,space_cache,subvol=@snapshots 0 0\" >> /etc/fstab && "
    "echo \"{BOOT_PART} /boot vfat defaults 0 2\" >> /etc/fstab && "
    "echo \"gentoo\" > /etc/hostname && "
    "echo \"root:password\" | chpasswd && "
    "emerge sys-boot/grub:2 && "
    "grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=gentoo && "
    "grub-mkconfig -o /boot/grub/grub.cfg && "
    "emerge --noreplace net-misc/netifrc && "
    "echo 'config_eth0=\"dhcp\"' > /etc/conf.d/net && "
    "ln -s /etc/init.d/net.lo /etc/init.d/net.eth0 && "
    "rc-update add net.eth0 default && "
    "emerge net-misc/dhcpcd && "
    "rc-update add dhcpcd default && "
    "emerge net-wireless/iw net-wireless/wpa_supplicant && "
    "rc-update add wpa_supplicant default && "
    "cat <<EOL > /etc/wpa_supplicant/wpa_supplicant.conf\n"
    "ctrl_interface=/var/run/wpa_supplicant\n"
    "ctrl_interface_group=wheel\n"
    "update_config=1\n"
    "network={\n"
    "ssid=\"your_SSID\"\n"
    "psk=\"your_password\"\n"
    "}\n"
    "EOL && "
    "echo 'wpa_supplicant_args=\"-c /etc/wpa_supplicant/wpa_supplicant.conf -D nl80211,wext -i wlan0\"' > /etc/conf.d/wpa_supplicant && "
    "ln -s /etc/init.d/net.lo /etc/init.d/net.wlan0 && "
    "rc-update add net.wlan0 default && "
    "rc-update add sshd default && "
    "rc-update add syslog-ng default && "
    "rc-update add cronie default'")])

debian_install = lambda: list(map(run_command, [
    f"debootstrap --arch amd64 bookworm {CHROOT_DIR} http://deb.debian.org/debian/",
    f"mount --bind /dev {CHROOT_DIR}/dev",
    f"mount --bind /proc {CHROOT_DIR}/proc",
    f"mount --bind /sys {CHROOT_DIR}/sys"
])) + [run_command(f"chroot {CHROOT_DIR} /bin/bash -c '"
    "ln -sf /usr/share/zoneinfo/UTC /etc/localtime && "
    "dpkg-reconfigure -f noninteractive tzdata && "
    "echo \"en_US.UTF-8 UTF-8\" > /etc/locale.gen && "
    "locale-gen && "
    "echo \"LANG=en_US.UTF-8\" > /etc/default/locale && "
    "echo \"debian\" > /etc/hostname && "
    "apt-get install -y network-manager && "
    "systemctl enable NetworkManager && "
    "apt-get install -y grub-efi && "
    "grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=debian && "
    "update-grub'")])

alpine_install = lambda: list(map(run_command, [
    f"apk add --root {CHROOT_DIR} --initdb alpine-base",
    f"echo \"{ROOT_PART} / btrfs noatime,compress=zstd,space_cache,subvol=@root 0 0\" > {CHROOT_DIR}/etc/fstab",
    f"echo \"{ROOT_PART} /home btrfs noatime,compress=zstd,space_cache,subvol=@home 0 0\" >> {CHROOT_DIR}/etc/fstab",
    f"echo \"{ROOT_PART} /.snapshots btrfs noatime,compress=zstd,space_cache,subvol=@snapshots 0 0\" >> {CHROOT_DIR}/etc/fstab",
    f"echo \"{BOOT_PART} /boot vfat defaults 0 2\" >> {CHROOT_DIR}/etc/fstab"
])) + [run_command(f"chroot {CHROOT_DIR} /bin/sh -c '"
    "ln -sf /usr/share/zoneinfo/UTC /etc/localtime && "
    "echo \"en_US.UTF-8 UTF-8\" > /etc/locale.gen && "
    "echo \"LANG=en_US.UTF-8\" > /etc/profile.d/locale.sh && "
    "echo \"alpine\" > /etc/hostname && "
    "rc-update add networking && "
    "apk add --no-cache grub && "
    "grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=alpine && "
    "grub-mkconfig -o /boot/grub/grub.cfg'")])

cleanup = lambda: list(map(run_command, [
    f"umount -l {CHROOT_DIR}/dev{/shm,/pts,}",
    f"umount -R {CHROOT_DIR}"
]))

main = lambda: list(
    map(
        lambda x: x,
        [
            partition_disk,
            format_and_mount,
            (lambda distro: {
                "arch": arch_install,
                "gentoo": gentoo_install,
                "debian": debian_install,
                "alpine": alpine_install
            }.get(distro, lambda: exit(1))()),
            cleanup
        ]
    )
)

if __name__ == "__main__":
    main()
    
