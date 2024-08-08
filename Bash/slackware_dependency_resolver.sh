#!/bin/sh
set -euo pipefail

# Configuration
SBO_REPO_URL="https://slackbuilds.org/slackbuilds/14.2"
TEMP_DIR="/tmp/slackbuilds"
INSTALLED_PACKAGES="/var/log/installed_packages.log"
DOWNLOADS_LOG="/var/log/downloads.log"
INSTALL_LOG="/var/log/install.log"

# Logging function
log() {
  local message=$1
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> "$INSTALL_LOG"
}

# Download package files
download_package_files() {
  local package_name=$1
  local package_url="$SBO_REPO_URL/$package_name"
  local package_dir="$TEMP_DIR/$package_name"

  log "Downloading package files for $package_name"
  mkdir -p "$package_dir"
  wget -q -P "$package_dir" "$package_url/$package_name.info" 2>> "$DOWNLOADS_LOG"
  wget -q -P "$package_dir" "$package_url/$package_name.SlackBuild" 2>> "$DOWNLOADS_LOG"

  if [ ! -f "$package_dir/$package_name.info" ] || [ ! -f "$package_dir/$package_name.SlackBuild" ]; then
    log "Failed to download package files for $package_name."
    rm -rf "$package_dir"
    return 1
  fi
  log "Files downloaded to $package_dir"
  return 0
}

# Resolve dependencies
resolve_dependencies() {
  local package_dir=$1
  local info_file="$package_dir/${package_dir##*/}.info"
  local dependencies=""

  if [ -f "$info_file" ]; then
    dependencies=$(grep "^REQUIRES" "$info_file" | cut -d '"' -f 2)
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
    log "No missing libraries found."
    return 0
  fi

  log "Attempting to install missing libraries: $missing_libs"
  for lib in $missing_libs; do
    pkg_name=$(slackpkg file-search "$lib" 2>/dev/null | grep "^  [^ ]" | awk '{print $1}' || true)

    if [ -n "$pkg_name" ]; then
      log "Installing package $pkg_name for missing library $lib"
      slackpkg install "$pkg_name" 2>> "$INSTALL_LOG"
    else
      log "Could not find a package providing the library $lib. Please check manually."
    fi
  done
}

# Install package
install_package() {
  local package_dir=$1
  local package_name=${package_dir##*/}

  if grep -q "^$package_name$" "$INSTALLED_PACKAGES"; then
    log "Package $package_name already installed. Skipping."
    return
  fi

  log "Installing package: $package_name"
  chmod +x "$package_dir/$package_name.SlackBuild"
  "$package_dir/$package_name.SlackBuild" >> "$INSTALL_LOG" 2>&1

  find "$package_dir" -type f -executable | while read -r binary; do
    log "Checking $binary for missing libraries..."
    missing_libs=$(check_missing_libs "$binary")
    install_missing_libs "$missing_libs"
  done

  echo "$package_name" >> "$INSTALLED_PACKAGES"
  log "Package $package_name installed successfully."
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
if [ "$#" -eq 0 ]; then
  echo "Usage: $0 <package-name> [<package-name>...]"
  exit 1
fi

# Ensure log files exist and are writable
mkdir -p "$(dirname "$INSTALLED_PACKAGES")"
touch "$INSTALLED_PACKAGES" "$INSTALL_LOG" "$DOWNLOADS_LOG"

for package in "$@"; do
  # Validate package name
  if ! validate_package_name "$package"; then
    echo "Skipping invalid package name: $package"
    continue
  fi

  log "Resolving dependencies for package: $package"

  if ! download_package_files "$package"; then
    log "Skipping $package due to download failure."
    continue
  fi

  package_dir="$TEMP_DIR/$package"

  info_dependencies=$(resolve_dependencies "$package_dir")

  if [ -n "$info_dependencies" ]; then
    log "Info file dependencies for $package: $info_dependencies"
    for dep in $info_dependencies; do
      if validate_package_name "$dep"; then
        "$0" "$dep"
      else
        log "Invalid dependency name: $dep"
      fi
    done
  else
    log "No info file dependencies found for $package."
  fi

  install_package "$package_dir"
done

rm -rf "$TEMP_DIR"
log "All packages and dependencies have been processed."
