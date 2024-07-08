#!/bin/sh

netstat -an | grep -E "ESTABLISHED|LISTEN" || echo "Warning: No established or listening network connections found."
uptime || echo "Error: Unable to check system load."
ps -eo pid,%cpu,%mem,cmd --sort=-%cpu,-%mem | awk '$2 >= 50 || $3 >= 50 { print $0 }' || echo "No processes with high CPU or memory usage found."

case "$(uname -s)" in
    Linux)
        md5sum /bin/* /sbin/* /usr/bin/* /usr/sbin/* 2>/dev/null || echo "Error: Unable to check file integrity."
        grep -Ei "error|warn|fail|denied" /var/log/messages /var/log/syslog 2>/dev/null || echo "No suspicious activities found in system logs."
        ;;
    FreeBSD)
        md5 -q /bin/* /sbin/* /usr/bin/* /usr/sbin/* 2>/dev/null || echo "Error: Unable to check file integrity."
        grep -Ei "error|warn|fail|denied" /var/log/messages /var/log/all.log 2>/dev/null || echo "No suspicious activities found in system logs."
        ;;
esac

ss -tuln | grep "sshd" || echo "Warning: SSH daemon (sshd) not found or no open SSH ports."
ps aux | grep -v "^USER" | grep -v "grep" || echo "No background processes found."

echo "Security check completed."
