# Setting Up Xubuntu 24.04 LTS with BTRFS:

This guide helps you set up Xubuntu 24.04 LTS using BTRFS on low-end hardware. BTRFS offers powerful features like snapshots and rollback, making system maintenance and recovery effortless.

## Prerequisites

Ensure you have:

- Xubuntu 24.04 LTS installed (or upgraded from a previous version).
- Basic familiarity with the command line.

## Steps

1. **Partitioning**:
   - During installation, choose the "Something else" option for partitioning.
   - Create BTRFS subvolumes for your root filesystem:
     ```bash
     sudo btrfs subvolume create /mnt/@root
     sudo btrfs subvolume create /mnt/@home
     ```
   - Set the mount point to `/` for `@root` and `/home` for `@home`.

2. **Installing BTRFS Tools**:
   - After installation, open a terminal.
   - Install the BTRFS tools:
     ```bash
     sudo apt update
     sudo apt install btrfs-progs
     ```

3. **Snapshots and Rollback**:
   - Take a snapshot before making system changes (e.g., updates):
     ```bash
     sudo btrfs subvolume snapshot /mnt/@root /mnt/@snap1
     ```
   - Roll back to a snapshot if needed:
     ```bash
     sudo btrfs subvolume delete /mnt/@root
     sudo btrfs subvolume snapshot /mnt/@snap1 /mnt/@root
     ```

4. **System Checks**:
   - Check BTRFS status:
     ```bash
     sudo btrfs filesystem df /
     ```
   - Monitor disk usage:
     ```bash
     sudo btrfs filesystem usage /
     ```

## BTRFS vs. LVM

- **BTRFS**:
  - Modern filesystem with features like snapshots, compression, and RAID.
  - Highly scalable (supports up to 16 exabytes of storage).
  - Efficient with SSDs.
  - Handles large numbers of files and directories effectively.
- **LVM**:
  - Focuses on space allocation.
  - Well-established and stable.
  - Limited to 2 terabytes.
  - Works well with ext4.

## Tips for Optimizing BTRFS

- Enable compression for potential space savings:
  ```bash
  sudo btrfs filesystem defragment -r -czstd /
  ```
- Regularly balance data across devices:
  ```bash
  sudo btrfs balance start /
  ```

## Conclusion

Congratulations on setting up Xubuntu with BTRFS
