#!/bin/bash

# System administration script

# Setting variables

myvar="Hello, world!"

# Display system information

echo "Hostname: $(hostname)"

uname -a

# Check disk space

threshold=90

df -h | awk '{print $1,$5}' | while read output;

do

    usep=$(echo $output | awk '{print $2}' | cut -d'%' -f1)

    if [ $usep -gt $threshold ]; then

        echo "Low disk space on drive $(echo $output | awk '{print $1}') ($usep% used)"

    fi

done

# Backup files

backupdir="/backup"

source="/data"

date=$(date +"%Y%m%d")

mkdir -p $backupdir

rsync -a $source $backupdir/$date

# Restart service

service="myservice"

status="stopped"

systemctl is-active --quiet $service && (

    systemctl start $service

    echo "Service $service restarted"

) || (

    echo "Service $service already running"

)

# Running external programs

echo "Running ls command:"

ls

echo "Running ping command:"

ping -c 3 localhost

# Virtual machine management (Azure)

resourcegroup="myresourcegroup"

vmname="myvm"

vmimage="UbuntuLTS"

vmsize="Standard_D2s_v3"

adminuser="myadminuser"

adminpassword="mypassword"

location="westus2"

# Create a new VM in Azure

echo "Creating a new VM in Azure..."

az group create --name $resourcegroup --location $location

az vm create --resource-group $resourcegroup --name $vmname --image $vmimage --size $vmsize --admin-username $adminuser --admin-password $adminpassword

# Configuration management (PowerShell DSC)

echo "Applying configuration using PowerShell DSC..."

echo "Configuration MyConfig { Node '$(hostname)' { WindowsFeature IIS { Ensure = 'Present' } } }" > MyConfig.ps1

sudo pwsh -Command "& {Import-DSCResource -ModuleName PSDesiredStateConfiguration; MyConfig | Start-DscConfiguration -Wait -Verbose}"

# Real-time monitoring (Performance Monitor)

echo "Monitoring system performance with Performance Monitor..."

gnome-system-monitor &

# Security management (Event Viewer)

echo "Monitoring security events with Event Viewer..."

gnome-system-log --priority=2 &

# Disaster recovery (Veeam Backup)

echo "Backing up critical data with Veeam Backup..."

sudo veeamzip -r $backupdir/$date -t full -s $source

# Remote administration (SSH)

echo "Executing command on remote system with SSH..."

ssh remotesystem "ls -l"

# Functions

myfunc() {

    echo $myvar

}

# Call function

myfunc

