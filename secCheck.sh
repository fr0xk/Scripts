#!/bin/sh

# This script performs a comprehensive security vulnerability check on a Linux desktop system without installing external tools.

# Update package lists

sudo apt-get update

# Check for security updates

sudo apt-get upgrade

# Check for open ports

sudo netstat -tulpn

# Check for rootkits

sudo ls -alh /usr/bin/.sshd

sudo ls -alh /usr/sbin/.sshd

sudo ls -alh /usr/bin/.sshd

sudo ps aux | awk '{print $11}' | grep "^/"

# Check for suspicious files in user directories

sudo find /home -name "*.sh" -o -name "*.py" -o -name "*.pl" | xargs grep -l "rm -rf /"

# Check for unauthorized sudo access

sudo grep -E '^sudo:.*(ALL|\(ALL\))' /etc/group | cut -d':' -f4 | tr ',' '\n' | while read user; do sudo -lU "$user"; done | grep -v 'may run the following commands' || echo "No unauthorized sudo access found"

# Check for common attack vectors

sudo grep -r "wget http" /var/log/

sudo grep -r "curl http" /var/log/

sudo grep -r "gcc -o" /var/log/

sudo grep -r "rm -rf /" /var/log/

sudo grep -r "chmod 777" /var/log/

# Check for malware and viruses

sudo find /home -type f \( -iname "*.exe" -o -iname "*.dll" -o -iname "*.bat" -o -iname "*.vbs" -o -iname "*.ps1" \) -print0 | xargs -0 -I{} file -b {} | grep -v script | awk -F: '{print $1}' | xargs clamscan -i

# Display results

echo "Security vulnerability check completed"

