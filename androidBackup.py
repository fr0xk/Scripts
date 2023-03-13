import os

import subprocess

# Change this to the directory where you want to store the backups

backup_dir = "/storage/emulated/0/backups"

# Create the backup directory if it doesn't already exist

if not os.path.exists(backup_dir):

    os.mkdir(backup_dir)

# Get a list of all installed packages on the device

package_list = subprocess.check_output(["pm", "list", "packages", "-f"]).decode("utf-8").splitlines()

# Loop through the packages and backup their APK and data (if possible)

for package in package_list:

    package = package.strip()[8:]

    apk_path = subprocess.check_output(["pm", "path", package]).decode("utf-8").strip()[8:]

    apk_name = apk_path.split("/")[-1]

    backup_path = os.path.join(backup_dir, apk_name)

    with open(apk_path, "rb") as apk_file, open(backup_path, "wb") as backup_file:

        backup_file.write(apk_file.read())

    data_dir = subprocess.check_output(["pm", "dump", package]).decode("utf-8").splitlines()

    data_dir = [line for line in data_dir if "dataDir=" in line]

    if data_dir:

        data_dir = data_dir[0].split("=")[-1].strip()

        data_backup_path = os.path.join(backup_dir, f"{package}.tar.gz")

        with subprocess.Popen(["tar", "-czvf", data_backup_path, data_dir], stdout=subprocess.PIPE) as proc:

            output, error = proc.communicate()

            if error:

                print(f"Error backing up data for package {package}: {error}")

