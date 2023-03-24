@echo off

REM System administration script

REM Setting variables

set myvar="Hello, world!"

REM Display system information

echo "Hostname: %computername%"

systeminfo | findstr /i /c:"OS Name" /c:"OS Version"

REM Check disk space

set threshold=90

for /f "usebackq skip=1 tokens=1-3" %%A in (`wmic logicaldisk get caption^,size^,freespace`) do (

    if not "%%A"=="Caption" (

        set /a size=%%B/1024/1024

        set /a free=%%C/1024/1024

        set /a used=size-free

        set /a pct=used*100/size

        if %pct% gtr %threshold% (

            echo "Low disk space on drive %%A (%pct%% used)"

        )

    )

)

REM Backup files

set backupdir=C:\backup

set source=C:\data

set date=%date:~10,4%%date:~4,2%%date:~7,2%

if not exist %backupdir% mkdir %backupdir%

xcopy /s /e /y %source% %backupdir%\%date%

REM Restart service

set service=MyService

set status=stopped

sc query %service% | findstr /i /c:"%status%" && (

    net start %service%

    echo "Service %service% restarted"

) || (

    echo "Service %service% already running"

)

REM Running external programs

echo "Running dir command:"

dir

echo "Running ping command:"

ping localhost

REM Virtual machine management (Azure)

set resourcegroup=myresourcegroup

set vmname=myvm

set vmimage=UbuntuLTS

set vmsize=Standard_D2s_v3

set adminuser=myadminuser

set adminpassword=mypassword

set location=westus2

REM Create a new VM in Azure

echo "Creating a new VM in Azure..."

az group create --name %resourcegroup% --location %location%

az vm create --resource-group %resourcegroup% --name %vmname% --image %vmimage% --size %vmsize% --admin-username %adminuser% --admin-password %adminpassword%

REM Configuration management (PowerShell DSC)

echo "Applying configuration using PowerShell DSC..."

powershell.exe -ExecutionPolicy Bypass -Command "& {Import-DSCResource -ModuleName PSDesiredStateConfiguration; Configuration MyConfig { Node '%computername%' { WindowsFeature IIS { Ensure = 'Present' } } } MyConfig | Start-DscConfiguration -Wait -Verbose}"

REM Real-time monitoring (Performance Monitor)

echo "Monitoring system performance with Performance Monitor..."

perfmon /sys

REM Security management (Event Viewer)

echo "Monitoring security events with Event Viewer..."

eventvwr /c:Security

REM Disaster recovery (Veeam Backup)

echo "Backing up critical data with Veeam Backup..."

powershell.exe -ExecutionPolicy Bypass -Command "& {Add-PSSnapin VeeamPSSnapIn; Start-VBRZip -Entity '%source%' -Folder %backupdir% -CompressionLevel High -CompressionMode LZNT1 -AutoDelete 'Yes' -DeleteRevisions '1 month' -Description 'Daily backup'}"

REM Remote administration (PsExec)

echo "Executing command on remote system with PsExec..."

psexec \\remotesystem cmd.exe /c dir

REM Functions

:myfunc

echo %myvar%

goto :eof

