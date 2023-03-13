#!/data/data/com.termux/files/usr/bin/env python

import os

import shutil

import subprocess

import sys

# Check if device is rooted

def is_rooted():

    try:

        os.stat("/system/bin/su")

        return True

    except FileNotFoundError:

        return False

# Get the list of installed packages

def get_installed_packages():

    packages = []

    try:

        output = subprocess.check_output(["pm", "list", "packages", "-f"]).decode("utf-8").splitlines()

        for line in output:

            package = {}

            package["name"] = line.split("=")[-1]

            package["apk_path"] = line.split("=")[0].replace("package:/", "")

            packages.append(package)

    except subprocess.CalledProcessError:

        sys.exit("Error: Unable to get list of installed packages")

    return packages

# Get the package installer for a given package name

def get_package_installer(package_name):

    try:

        output = subprocess.check_output(["pm", "dump", package_name]).decode("utf-8")

        if "installerPackageName=" in output:

            installer = output.split("installerPackageName=")[-1].split()[0]

            return installer

    except subprocess.CalledProcessError:

        pass

    return None

# Backup the APK file for a given package

def backup_package(package):

    backup_dir = "/storage/emulated/0/backups"

    if not os.path.exists(backup_dir):

        os.makedirs(backup_dir)

    backup_file = os.path.join(backup_dir, package["name"] + ".apk")

    try:

        if is_rooted() or get_package_installer(package["name"]) != "com.android.vending":

            shutil.copyfile(package["apk_path"], backup_file)

        else:

            subprocess.check_call(["termux-setup-storage"])

            subprocess.check_call(["termux-clipboard-set", "granted"])

            subprocess.check_call(["termux-open", "intent:#Intent;action=android.settings.action.MANAGE_APP_PERMISSION;category=android.intent.category.DEFAULT;data=package:com.termux;end"])

            input("Grant the permission to access installed apps, then press Enter to continue...")

            apk_file = subprocess.check_output(["pm", "path", package["name"]]).decode("utf-8").strip().split(":")[-1]

            shutil.copyfile(apk_file, backup_file)

        print(f"Backed up APK file for {package['name']} to {backup_file}")

    except (subprocess.CalledProcessError, OSError):

        print(f"Error: Unable to backup APK file for {package['name']}")

# Get the list of installed packages and backup their APK files

packages = get_installed_packages()

for package in packages:

    backup_package(package)

