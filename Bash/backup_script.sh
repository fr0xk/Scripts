#!/bin/bash

# Set the backup source and destination directories
SRC="/"
DEST="/mnt/backup"
LOG_FILE="/path/to/backup.log"

# Exclude specific directories
EXCLUDE=(
  "--exclude=/dev/*"
  "--exclude=/proc/*"
  "--exclude=/sys/*"
  "--exclude=/tmp/*"
  "--exclude=/run/*"
  "--exclude=/mnt/*"
  "--exclude=/media/*"
)

# Function to check available space
function check_space {
  local space_threshold=20  # Adjust threshold as needed (e.g., 20%)
  local available_percent=$(df --output=pcent $DEST | tail -n 1 | tr -d ' %')

  if [[ $available_percent -ge $((100 - $space_threshold)) ]]; then
    echo "Warning: Less than $space_threshold% free space in $DEST. Backup may not complete."
    return 1  # Indicate potential issue
  fi
  return 0  # Indicate sufficient space
}

# Check destination directory and free space
if [[ ! -d $DEST ]]; then
  echo "Error: Destination directory $DEST does not exist."
  exit 1
fi

if ! mountpoint -q $DEST; then
  echo "Error: Destination $DEST is not mounted."
  exit 1
fi

if ! check_space; then
  # Prompt for confirmation or exit based on your needs (e.g., read -p "Continue? (y/n): ")
  exit 1
fi

# Ensure log directory exists
if [[ ! -d $(dirname "$LOG_FILE") ]]; then
  echo "Error: Log directory $(dirname "$LOG_FILE") does not exist."
  exit 1
fi

# Run rsync with archive, verbose, delete, exclude options and log output
rsync -avz "${EXCLUDE[@]}" "$SRC" "$DEST" >> "$LOG_FILE" 2>&1

# Check exit code and provide feedback
if [[ $? -eq 0 ]]; then
  echo "Backup completed successfully."
else
  echo "Backup failed with exit code: $?."
fi
