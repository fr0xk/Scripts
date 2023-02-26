#!/bin/bash

# Set variables
USERNAME='user'
VENV_NAME='env'
DESKTOP_ENVIRONMENT='lxqt'

# Check if script is being run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Partition the disk and create LVM volumes
printf "o\nn\np\n1\n\n\nw\n" | fdisk /dev/sda || { echo "Failed to partition disk"; exit 1; }
pvcreate /dev/sda1 || { echo "Failed to create physical volume"; exit 1; }
vgcreate $VG_NAME /dev/sda1 || { echo "Failed to create volume group"; exit 1; }
lvcreate -n $LV_ROOT_NAME -L 100%FREE $VG_NAME || { echo "Failed to create logical volume"; exit 1; }

# Format the partitions
mkfs.ext4 /dev/$VG_NAME/$LV_ROOT_NAME || { echo "Failed to format root partition"; exit 1; }
mkswap /dev/sda1 || { echo "Failed to create swap partition"; exit 1; }
swapon /dev/sda1 || { echo "Failed to activate swap partition"; exit 1; }

# Mount the file systems
mount /dev/$VG_NAME/$LV_ROOT_NAME /mnt || { echo "Failed to mount root partition"; exit 1; }
mkdir -p /mnt/{boot,dev,proc,sys} || { echo "Failed to create mount points"; exit 1; }
mount /dev/sda1 /mnt/boot || { echo "Failed to mount boot partition"; exit 1; }
mount --bind /dev /mnt/dev || { echo "Failed to bind /dev"; exit 1; }
mount --bind /proc /mnt/proc || { echo "Failed to bind /proc"; exit 1; }
mount --bind /sys /mnt/sys || { echo "Failed to bind /sys"; exit 1; }

# Install Debian Sid from minimal bootable drive
debootstrap sid /mnt http://deb.debian.org/debian || { echo "Failed to install Debian Sid"; exit 1; }

# Configure the system
echo "127.0.0.1 $(hostname)" >> /mnt/etc/hosts || { echo "Failed to configure hosts file"; exit 1; }
echo "LANG=en_US.UTF-8" > /mnt/etc/locale.conf || { echo "Failed to configure locale"; exit 1; }
chroot /mnt /bin/bash -c "locale-gen en_US.UTF-8" || { echo "Failed to generate locale"; exit 1; }
echo "root:password" | chroot /mnt /usr/sbin/chpasswd || { echo "Failed to set root password"; exit 1; }
echo "$USERNAME:password" | chroot /mnt /usr/sbin/chpasswd || { echo "Failed to set user password"; exit 1; }
chroot /mnt /bin/bash -c "usermod -aG sudo $USERNAME" || { echo "Failed to add user to sudo group"; exit 1; }
chroot /mnt /bin/bash -c "echo $VENV_NAME > /etc/virtualenv" || { echo "Failed to create virtual environment file"; exit 1; }

 # Activate the virtual environment and install necessary Python packages
chroot /mnt /bin/bash -c "source /home/$USERNAME/$VENV_NAME/bin/activate && pip3 install numpy pandas matplotlib jupyter scikit-learn" || { echo "Failed to install Python packages"; exit 1; }

# Configure the bash prompt
echo 'PS1="\[\033[38;5;214m\]\u@\h:\[\033[38;5;33m\]\w\[\033[0m\]\$ "' >> /mnt/etc/bash.bashrc || { echo "Failed to configure bash prompt"; exit 1; }

# Configure the sound and video environment
echo "options snd-hda-intel dmic_detect=0" >> /mnt/etc/modprobe.d/sound.conf || { echo "Failed to configure sound"; exit 1; }
echo "Section \"Device\"\n\tIdentifier \"Intel Graphics\"\n\tDriver \"intel\"\nEndSection" > /mnt/etc/X11/xorg.conf.d/20-intel.conf || { echo "Failed to configure video"; exit 1; }

# Install desktop environment
chroot /mnt /bin/bash -c "apt-get update && apt-get install -y $DESKTOP_ENVIRONMENT" || { echo "Failed to install desktop environment"; exit 1; }

# Clean up
umount -l /mnt/dev /mnt/proc /mnt/sys /mnt/boot /mnt || { echo "Failed to unmount file systems"; exit 1; }

# MIT License
cat <<EOF > /mnt/LICENSE
MIT License

Copyright (c) [year] [author]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
