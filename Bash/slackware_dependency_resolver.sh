#!/bin/sh
set -euo pipefail

# Configuration
SBO_REPO_URL="https://slackbuilds.org/slackbuilds/14.2"
TEMP_DIR="/tmp/slackbuilds"
INSTALLED_PACKAGES="/var/log/installed_packages.log"
DOWNLOADS_LOG="/var/log/downloads.log"
INSTALL_LOG="/var/log/install.log"
REMOVE_LOG="/var/log/remove.log"

# Logging function
log() {
  local log_file=$1
  local message=$2
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> "$log_file"
}

# Download package files
download_package_files() {
  local package_name=$1
  local package_url="$SBO_REPO_URL/$package_name"
  local package_dir="$TEMP_DIR/$package_name"

  log "$DOWNLOADS_LOG" "Downloading package files for $package_name"
  mkdir -p "$package_dir"
  wget -q -P "$package_dir" "$package_url/$package_name.info" 2>> "$DOWNLOADS_LOG"
  wget -q -P "$package_dir" "$package_url/$package_name.SlackBuild" 2>> "$DOWNLOADS_LOG"

  if [ ! -f "$package_dir/$package_name.info" ] || [ ! -f "$package_dir/$package_name.SlackBuild" ]; then
    log "$INSTALL_LOG" "Failed to download package files for $package_name."
    rm -rf "$package_dir"
    return 1
  fi
  log "$INSTALL_LOG" "Files downloaded to $package_dir"
  return 0
}

# Resolve dependencies
resolve_dependencies() {
  local package_dir=$1
  local info_file="$package_dir/${package_dir##*/}.info"
  local dependencies=""

  if [ -f "$info_file" ]; then
    dependencies=$(grep "^REQUIRES" "$info_file" | cut -d '"' -f 2 || true)
  fi

  echo "$dependencies"
}

# Check for missing libraries
check_missing_libs() {
  local binary=$1
  local missing_libs=""

  if [ ! -f "$binary" ]; then
    return 0
  fi

  while read -r lib; do
    if echo "$lib" | grep -q "not found"; then
      missing_libs="$missing_libs $(echo "$lib" | awk '{print $1}')"
    fi
  done < <(ldd "$binary" 2>/dev/null || true)

  echo "$missing_libs"
}

# Install missing libraries
install_missing_libs() {
  local missing_libs=$1

  if [ -z "$missing_libs" ]; then
    log "$INSTALL_LOG" "No missing libraries found."
    return 0
  fi

  log "$INSTALL_LOG" "Attempting to install missing libraries: $missing_libs"
  for lib in $missing_libs; do
    pkg_name=$(slackpkg file-search "$lib" 2>/dev/null | grep "^  [^ ]" | awk '{print $1}' || true)

    if [ -n "$pkg_name" ]; then
      log "$INSTALL_LOG" "Installing package $pkg_name for missing library $lib"
      slackpkg install "$pkg_name" 2>> "$INSTALL_LOG"
    else
      log "$INSTALL_LOG" "Could not find a package providing the library $lib. Please check manually."
    fi
  done
}

# Install package
install_package() {
  local package_dir=$1
  local package_name=${package_dir##*/}

  if grep -q "^$package_name$" "$INSTALLED_PACKAGES"; then
    log "$INSTALL_LOG" "Package $package_name already installed. Skipping."
    return
  fi

  log "$INSTALL_LOG" "Installing package: $package_name"
  chmod +x "$package_dir/$package_name.SlackBuild"
  "$package_dir/$package_name.SlackBuild" >> "$INSTALL_LOG" 2>&1

  find "$package_dir" -type f -executable | while read -r binary; do
    log "$INSTALL_LOG" "Checking $binary for missing libraries..."
    missing_libs=$(check_missing_libs "$binary")
    install_missing_libs "$missing_libs"
  done

  echo "$package_name" >> "$INSTALLED_PACKAGES"
  log "$INSTALL_LOG" "Package $package_name installed successfully."
}

# Remove package
remove_package() {
  local package_name=$1

  if ! grep -q "^$package_name$" "$INSTALLED_PACKAGES"; then
    log "$REMOVE_LOG" "Package $package_name is not installed. Skipping removal."
    return
  fi

  log "$REMOVE_LOG" "Removing package: $package_name"
  # Assuming the removal command is `slackpkg remove` (replace with actual command if needed)
  slackpkg remove "$package_name" >> "$REMOVE_LOG" 2>&1

  sed -i "/^$package_name$/d" "$INSTALLED_PACKAGES"
  log "$REMOVE_LOG" "Package $package_name removed successfully."
}

# Cleanup unneeded dependencies
cleanup_dependencies() {
  local package_name=$1
  local dependencies=$(resolve_dependencies "$TEMP_DIR/$package_name")

  for dep in $dependencies; do
    if ! grep -q "^$dep$" "$INSTALLED_PACKAGES"; then
      log "$REMOVE_LOG" "Dependency $dep is no longer needed. Removing."
      remove_package "$dep"
    fi
  done
}

# Validate package name
validate_package_name() {
  local package_name=$1
  if ! echo "$package_name" | grep -Eq '^[a-zA-Z0-9_-]+$'; then
    echo "Invalid package name: $package_name"
    return 1
  fi
  return 0
}

# Main execution
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <install|remove> <package-name> [<package-name>...]"
  exit 1
fi

action=$1
shift

# Ensure log files exist and are writable
mkdir -p "$(dirname "$INSTALLED_PACKAGES")"
touch "$INSTALLED_PACKAGES" "$INSTALL_LOG" "$DOWNLOADS_LOG" "$REMOVE_LOG"

for package in "$@"; do
  # Validate package name
  if ! validate_package_name "$package"; then
    echo "Skipping invalid package name: $package"
    continue
  fi

  case $action in
    install)
      log "$INSTALL_LOG" "Resolving dependencies for package: $package"

      if ! download_package_files "$package"; then
        log "$INSTALL_LOG" "Skipping $package due to download failure."
        continue
      fi

      package_dir="$TEMP_DIR/$package"

      info_dependencies=$(resolve_dependencies "$package_dir")

      if [ -n "$info_dependencies" ]; then
        log "$INSTALL_LOG" "Info file dependencies for $package: $info_dependencies"
        for dep in $info_dependencies; do
          if validate_package_name "$dep"; then
            "$0" install "$dep"
          else
            log "$INSTALL_LOG" "Invalid dependency name: $dep"
          fi
        done
      else
        log "$INSTALL_LOG" "No info file dependencies found for $package."
      fi

      install_package "$package_dir"
      ;;
    remove)
      remove_package "$package"
      cleanup_dependencies "$package"
      ;;
    *)
      echo "Invalid action: $action. Use 'install' or 'remove'."
      exit 1
      ;;
  esac
done

rm -rf "$TEMP_DIR"
log "$INSTALL_LOG" "All specified actions have been processed."
