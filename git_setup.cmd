@echo off

set /p git_username=Enter your Git username:

set /p git_email=Enter your Git email address:

git config --global user.name "%git_username%"

git config --global user.email "%git_email%"

set /p ssh_key_filename=Enter the new SSH key filename (e.g. id_ed25519_github):

move %USERPROFILE%\.ssh\id_rsa %USERPROFILE%\.ssh\%ssh_key_filename%

ssh-keygen -t ed25519 -C "%git_email%" -f %USERPROFILE%\.ssh\%ssh_key_filename% -q -N ""

icacls %USERPROFILE%\.ssh\%ssh_key_filename% /c /t /inheritance:r

icacls %USERPROFILE%\.ssh\%ssh_key_filename% /c /t /grant:r "%USERNAME%":R

icacls %USERPROFILE%\.ssh\%ssh_key_filename%.pub /c /t /inheritance:r

icacls %USERPROFILE%\.ssh\%ssh_key_filename%.pub /c /t /grant:r "%USERNAME%":R

@echo Please add the following SSH key to your GitHub account:

type %USERPROFILE%\.ssh\%ssh_key_filename%.pub

set /p repo_url=Enter the GitHub repository URL (e.g. git@github.com:<username>/<repository>.git):

set /p repo_path=Enter the local path where you want to clone the repository (e.g. C:\Users\<username>\my_repository):

cd /d "%repo_path%"

git clone %repo_url% .

git pull

echo # My Project > README.md

echo. >> README.md

echo This is my project. >> README.md

git add README.md

git commit -m "Add README.md"

git push

ssh-add -D %USERPROFILE%\.ssh\%ssh_key_filename%

