#!/bin/sh

# Define required packages

required_packages="x11-repo xorg-server xorg-xsetroot xorg-xrandr xterm mpv xorg-server-xvfb aterm"

# Update the package list and install necessary packages

echo "Installing required packages..."

for package in $required_packages; do

    pkg install "$package"

done

# Set up the X session

echo "Starting X session..."

screen_size=$(termux-info | grep "Screen size" | awk '{print $3}')

Xvfb :1 -screen 0 "${screen_size}x768" -ac &

export DISPLAY=:1

xsetroot -solid "#000000"

xterm &




