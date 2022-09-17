### Library's ###
from os import system
from os import mkdir
from os import makedirs
from os import path
from os import remove
from platform import win32_ver
from urllib import request


### Install Chocolatey ### 
# system("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")


### Configure Terminal and Prompt ###
## Set up Drop Down Terminal ##
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/m2GrjeLPfcfqPrr/download/terminal.ico','/Users/ryan.rdvm/Pictures/terminal.ico')
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/bcrMyjQZg4yDiAH/download/Dropdown%20Terminal.lnk', '/Users/ryan.rdvm/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Windows PowerShell/Dropdown Terminal.lnk')


## Configure Powershell Prompt ##
# Install Oh-My-Posh
if not path.exists('/Users/ryan.rdvm/Documents/WindowsPowerShell/'):
    mkdir ('/Users/ryan.rdvm/Documents/WindowsPowerShell/')
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/aNncBdbZf8fzmDc/download/Theme.omp.json', '/Users/ryan.rdvm/Documents/WindowsPowerShell/Theme.omp.json')

system('choco install oh-my-posh -y')
system('choco install firacodenf -y')
# system('powershell.exe Set-ExecutionPolicy Unrestricted')

# Configure Ppowershell Profile
request.urlretrieve('https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/main/PowerShell_profile.ps1', '/Users/ryan.rdvm/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1')


## Configure Windows Terminal ##
if not path.exists('/Users/ryan.rdvm/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState'):
    makedirs('/Users/ryan.rdvm/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState')
    system('choco install microsoft-windows-terminal -y')

if not path.exists("/Users/ryan.rdvm/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"):
    request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/ywxdD6CFZFDB249/download/settings.json', '/Users/ryan.rdvm/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json')
else:
    remove("/Users/ryan.rdvm/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json")
    request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/ywxdD6CFZFDB249/download/settings.json', '/Users/ryan.rdvm/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json')


## WSL Configuration ##
#$WSL_Check=Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux | Select -ExpandProperty State # Caches the variable if WSL is enabled or not

#if($WSL_Check -eq "Enabled"){
#Invoke-WebRequest https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/test/Linux_Shell.sh -Outfile \\wsl$\Ubuntu\home\ryan.rdvm\Linux_Shell.sh
#wsl -u root chmod +x /home/ryan.rdvm/Linux_Shell.sh
#wsl -u root sh /home/ryan.rdvm/Linux_Shell.sh
#}


### Install Software ###
Packages = ["GoogleChrome", "putty", "winscp", "advanced-ipscanner", "git", "vscode", "vim", "sysinternals", "drawio", "powertoys", "googledrive", "vlc", "gsudo"]

for i in range(len(Packages)):
    temp = "choco install " + Packages[i] + " -y"
    system(temp)

system('choco install ringcentral-classic -y --ignore-checksum')