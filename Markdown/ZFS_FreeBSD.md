## Setting Up ZFS in FreeBSD (Including Modern SSDs)

1. **Install FreeBSD with ZFS**:
   - During installation, choose ZFS as the file system for your root partition.
   - If you're installing remotely, follow the instructions for creating a ZFS pool using the `zpool` command.

2. **Enable ZFS at Boot**:
   - Add the following line to `/etc/rc.conf`:
     ```
     zfs_enable="YES"
     ```
   - Start the ZFS service:
     ```
     # service zfs start
     ```

3. **Create a ZFS Pool**:
   - Assume you have three SSDs named `ada0`, `ada1`, and `ada2`.
   - Use the `zpool create` command to create a pool. For example:
     ```
     # zpool create mypool ada0 ada1 ada2
     ```

4. **Optimize for SSDs**:
   - Modern SSDs benefit from specific ZFS settings:
     - Set the `ashift` value to match the SSD's sector size (usually 12 for most SSDs):
       ```
       # zpool create -o ashift=12 mypool ada0 ada1 ada2
       ```
     - Enable TRIM support (if your SSD supports it):
       ```
       # zpool set autotrim=on mypool
       ```

5. **Taking Snapshots**:
   - To take a snapshot of your ZFS file system:
     ```
     $ cd /mnt/mypool
     $ zfs snapshot mypool@my_snapshot
     ```

6. **List Snapshots**:
   ```
   $ zfs list -t snapshot -r mypool
   ```

7. **Rollbacks**:
   - If something goes wrong, revert to a previous snapshot:
     ```
     $ zfs rollback mypool@my_snapshot
     ```
