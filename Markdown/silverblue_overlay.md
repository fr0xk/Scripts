
# Fedora Silverblue Overlay Management Script

This script automates the process of applying updates and configurations to a Fedora Silverblue system, leveraging its immutable architecture. It manages system modifications via an overlay filesystem and ensures that changes are applied in a new immutable deployment.

## Overview

Fedora Silverblue is an immutable desktop operating system where changes are managed using `rpm-ostree`. The script sets up an overlay filesystem, applies changes, and ensures that these changes are included in a new immutable deployment. 

## Key Concepts

- **Immutable System**: An operating system where core system files are protected from modification. Changes are managed through layered filesystems or containerized updates.
- **Overlay Filesystem**: A type of filesystem that combines a read-only lower layer (base system) with a writable upper layer (where changes are stored). It allows modifications to appear as if they were made directly to the base system.
- **`rpm-ostree`**: A tool used by Fedora Silverblue to manage system packages and create immutable deployments. It provides atomic upgrades and rollbacks.
- **`jq`**: A command-line tool for processing JSON data. While not used in this script, it's useful for interacting with JSON outputs from commands.

## Script Details

### 1. **Setup and Configuration**

The script begins by configuring error handling and defining essential paths:

```bash
set -euo pipefail

LOG_FILE="/var/log/overlay_script.log"
SWAY_CONFIG_TEMPLATE="/etc/sway/config.template"
OVERLAY_DIR="/var/lib/overlay"
MOUNT_POINT="/mnt"
```

- `set -euo pipefail`: Ensures the script exits on any command failure, usage of undefined variables, or pipeline failures.
- `LOG_FILE`: Path to the log file where script output is saved.
- `SWAY_CONFIG_TEMPLATE`: Path to the Sway configuration template.
- `OVERLAY_DIR`: Directory for the overlay filesystem.
- `MOUNT_POINT`: Directory where the overlay filesystem will be mounted.

### 2. **Logging Function**

The `log` function records messages with timestamps to both the console and a log file:

```bash
log() {
    local message="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" | tee -a "$LOG_FILE"
}
```

### 3. **Dependency Check**

Checks for the required commands:

```bash
check_dependencies() {
    local missing_dependencies=()
    for cmd in rpm-ostree jq; do
        if ! command -v "$cmd" &> /dev/null; then
            missing_dependencies+=("$cmd")
        fi
    done

    if [ ${#missing_dependencies[@]} -ne 0 ]; then
        log "Missing dependencies: ${missing_dependencies[*]}. Please install them first."
        exit 1
    fi
}
```

- Ensures that `rpm-ostree` and `jq` are installed. Exits with an error message if any required command is missing.

### 4. **Overlay Creation**

Sets up the overlay filesystem:

```bash
create_overlay() {
    log "Creating overlay directory."
    mkdir -p "$OVERLAY_DIR/upper" "$OVERLAY_DIR/work"
    mount -t overlay overlay -o lowerdir=/,upperdir="$OVERLAY_DIR/upper",workdir="$OVERLAY_DIR/work" "$MOUNT_POINT" || {
        log "Failed to mount overlay."
        exit 1
    }
}
```

- **`mkdir -p "$OVERLAY_DIR/upper" "$OVERLAY_DIR/work"`**: Creates the directories for the overlay filesystem.
- **`mount -t overlay overlay -o lowerdir=/,upperdir="$OVERLAY_DIR/upper",workdir="$OVERLAY_DIR/work" "$MOUNT_POINT"`**: Mounts the overlay filesystem with a read-only base layer (`lowerdir`), a writable layer (`upperdir`), and a work directory (`workdir`).

### 5. **Apply Overlay Changes**

Applies the overlay and binds the mount point:

```bash
apply_overlay_changes() {
    log "Applying overlay changes."
    mount --bind "$MOUNT_POINT" /mnt || {
        log "Failed to bind mount overlay."
        exit 1
    }
}
```

- **`mount --bind "$MOUNT_POINT" /mnt`**: Binds the overlay mount point to `/mnt`, allowing modifications to be accessible.

### 6. **Install Packages**

Installs specified packages into the overlay:

```bash
install_packages() {
    local packages="$1"
    if [ -z "$packages" ]; then
        log "No packages specified for installation."
        exit 1
    fi

    log "Installing packages: $packages."
    if rpm-ostree install $packages; then
        log "Packages installed successfully: $packages."
    else
        log "Failed to install packages: $packages."
        exit 1
    fi
}
```

- **`rpm-ostree install $packages`**: Installs the specified packages into the overlay.

### 7. **Set Font and DPI**

Updates the Sway configuration file:

```bash
set_font_dpi() {
    local font_size="$1"
    local dpi="$2"

    local sway_config="/mnt/etc/sway/config"

    if ! [[ "$font_size" =~ ^[0-9]+$ && "$dpi" =~ ^[0-9]+$ ]]; then
        log "Font size and DPI must be positive integers."
        exit 1
    fi

    if [ -f "$SWAY_CONFIG_TEMPLATE" ]; then
        sed "s/\$FONT_SIZE/$font_size/" "$SWAY_CONFIG_TEMPLATE" | sed "s/\$DPI/$dpi/" > "$sway_config"
        log "Sway configuration applied with font size $font_size and DPI $dpi."
    else
        log "Sway configuration template not found at $SWAY_CONFIG_TEMPLATE."
        exit 1
    fi
}
```

- **`sed "s/\$FONT_SIZE/$font_size/" "$SWAY_CONFIG_TEMPLATE"`**: Replaces placeholder `$FONT_SIZE` with the user-specified font size.
- **`sed "s/\$DPI/$dpi/"`**: Replaces placeholder `$DPI` with the user-specified DPI value.
- **`> "$sway_config"`**: Writes the updated configuration to the Sway config file.

### 8. **Commit and Deploy**

Commits the changes and prepares for reboot:

```bash
commit_and_deploy() {
    log "Committing changes to create a new deployment."
    if rpm-ostree ex livefs --commit; then
        log "Changes committed successfully."
    else
        log "Failed to commit changes."
        exit 1
    fi

    log "Rebooting to apply changes."
    cleanup_overlay
    reboot
}
```

- **`rpm-ostree ex livefs --commit`**: Commits changes to create a new immutable deployment.
- **`reboot`**: Reboots the system to apply the new deployment.

### 9. **Cleanup Overlay**

Cleans up after the operation:

```bash
cleanup_overlay() {
    log "Cleaning up overlay directory."
    umount "$MOUNT_POINT" || {
        log "Failed to unmount overlay."
        exit 1
    }
    rm -rf "$OVERLAY_DIR"
}
```

- **`umount "$MOUNT_POINT"`**: Unmounts the overlay filesystem.
- **`rm -rf "$OVERLAY_DIR"`**: Removes the overlay directory and its contents.

### 10. **Main Function**

Coordinates the overall workflow:

```bash
main() {
    check_dependencies

    create_overlay

    read -p "Enter packages to install (space-separated): " packages
    read -p "Enter font size: " font_size
    read -p "Enter DPI: " dpi

    apply_overlay_changes
    install_packages "$packages"
    set_font_dpi "$font_size" "$dpi"

    commit_and_deploy

    log "All operations completed successfully."
}
```

- Manages the sequence of operations, including dependency checks, overlay setup, package installation, configuration updates, and deployment.

## Usage

1. **Save the script** to a file, e.g., `update_silverblue.sh`.
2. **Make it executable**: `chmod +x update_silverblue.sh`
3. **Run the script**: `sudo ./update_silverblue.sh`

Ensure you have the necessary permissions and the script's requirements are met before execution.

## Full Script

```bash
#!/bin/bash

set -euo pipefail

LOG_FILE="/var/log/overlay_script.log"
SWAY_CONFIG_TEMPLATE="/etc/sway/config.template"
OVERLAY_DIR="/var/lib/overlay"
MOUNT_POINT="/mnt"

log() {
    local message="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" | tee -a "$LOG_FILE"
}

check_dependencies() {
    local missing_dependencies=()
    for cmd in rpm-ostree jq; do
        if ! command -v "$cmd" &> /dev/null; then
            missing_dependencies+=("$cmd")
        fi
    done

    if [ ${#missing_dependencies[@]} -ne 0 ]; then
        log "Missing dependencies: ${missing_dependencies[*]}. Please install them first."
        exit 1
    fi
}

create_overlay() {
    log "Creating overlay directory."
    mkdir -p "$OVERLAY_DIR/upper" "$OVERLAY_DIR/work"
    mount -t overlay overlay -o lowerdir=/,upperdir="$OVERLAY_DIR/upper",workdir="$OVERLAY_DIR/work" "$MOUNT_POINT" || {
        log "Failed to mount overlay."
        exit 1
    }
}

apply_overlay_changes() {
    log "Applying overlay changes."
    mount --bind "$MOUNT_POINT" /mnt || {
        log "Failed to bind mount overlay."
        exit 1
    }
}

install_packages() {
    local packages="$1"
    if [ -z "$packages" ]; then
        log "No packages specified for installation."
        exit 1
    fi

    log "Installing packages: $packages."
    if rpm-ostree install $packages; then
        log "Packages installed successfully: $packages."
    else
        log "Failed to install packages: $packages."
        exit 1
    fi
}

set_font_dpi() {
    local font_size="$1"
    local dpi="$2"

    local sway_config="/mnt/etc/sway/config"

    if ! [[ "$font_size" =~ ^[0-9]+$ && "$dpi" =~ ^[0-9]+$ ]]; then
        log "Font size and DPI must be positive integers."
        exit 1
    fi

    if [ -f "$SWAY_CONFIG_TEMPLATE" ]; then
        sed "s/\$FONT_SIZE/$font_size/" "$SWAY_CONFIG_TEMPLATE" | sed "s/\$DPI/$dpi/" > "$sway_config"
        log "Sway configuration applied with font size $font_size and DPI $dpi."
    else
        log "Sway configuration template not found at $SWAY_CONFIG_TEMPLATE."
        exit 1
    fi
}

commit_and_deploy() {
    log "Committing changes to create a new deployment."
    if rpm-ostree ex livefs --commit; then
        log "Changes committed successfully."
    else
        log "Failed to commit changes."
        exit 1
    fi

    log "Rebooting to apply changes."
    cleanup_overlay
    reboot
}

cleanup_overlay() {
    log "Cleaning up overlay directory."
    umount "$MOUNT_POINT" || {
        log "Failed to unmount overlay."
        exit 1
    }
    rm -rf "$OVERLAY_DIR"
}

main() {
    check_dependencies

    create_overlay

    read -p "Enter packages to install (space-separated): " packages
    read -p "Enter font size: " font_size
    read -p "Enter DPI: " dpi

    apply_overlay_changes
    install_packages "$packages"
    set_font_dpi "$font_size" "$dpi"

    commit_and_deploy

    log "All operations completed successfully."
}

main
