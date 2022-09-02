### Library's ###
from asyncore import write
from os import system
from os import mkdir
from os import makedirs
from os import path
from os import remove
from platform import win32_ver
from urllib import request


### Install Chocolatey ### 
system("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")


### Configure Terminal and Prompt ###
## Set up Drop Down Terminal ##
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/m2GrjeLPfcfqPrr/download/terminal.ico','/Users/ryan/Pictures/terminal.ico')
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/bcrMyjQZg4yDiAH/download/Dropdown%20Terminal.lnk', '/Users/ryan/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Windows PowerShell/Dropdown Terminal.lnk')

## Configure Powershell Prompt ##
# Install Oh-My-Posh
if not path.exists('/Users/ryan/Documents/WindowsPowerShell/'):
    mkdir ('/Users/ryan/Documents/WindowsPowerShell/')
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/aNncBdbZf8fzmDc/download/Theme.omp.json', '/Users/ryan/Documents/WindowsPowerShell/Theme.omp.json')

system('choco install oh-my-posh -y')
system('choco install firacodenf -y')
system('Set-ExecutionPolicy Unrestricted')

# Configure Ppowershell Profile
RPORT_PORT="3389"
RPORT_URL="Test.test"
request.urlretrieve('https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/test/PowerShell_profile.ps1', '/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1')

open("/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1", 'a').write("\n")
open("/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1", 'a').write("# Carrionspike Alias")
open("/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1", 'a').write("\n")
open("/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1", 'a').write("$CarrionSpike=")
open("/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1", 'a').write(RPORT_URL)
open("/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1", 'a').write(":")
open("/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1", 'a').write(RPORT_PORT)


## Configure Windows Terminal ##
if not path.exists('/Users/ryan/Documents/WindowsPowerShell/'):
    makedirs('/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState')

remove("/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json")
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/ywxdD6CFZFDB249/download/settings.json', '/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json')

system('choco install microsoft-windows-terminal -y')

## WSL Configuration ##
#$WSL_Check=Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux | Select -ExpandProperty State # Caches the variable if WSL is enabled or not

#if($WSL_Check -eq "Enabled"){
#Invoke-WebRequest https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/test/Linux_Shell.sh -Outfile \\wsl$\Ubuntu\home\ryan\Linux_Shell.sh
#wsl -u root chmod +x /home/ryan/Linux_Shell.sh
#wsl -u root sh /home/ryan/Linux_Shell.sh
#}



### Install Software ###
Packages = ["GoogleChrome", "putty", "winscp", "advanced-ipscanner", "git", "vscode", "vim", "sysinternals", "drawio", "gimp", "powertoys", "googledrive", "vlc", "gsudo"]

for i in range(len(Packages)):
    temp = "choco install " + Packages[i] + " -y"
    system(temp)

system('choco install ringcentral-classic -y --ignore-checksum')

# system('choco install GoogleChrome -y')

# system('choco install putty -y')

# system('choco install winscp -y')

# system('choco install advanced-ipscanner -y')

# system('choco install git -y')

# system('choco install vscode -y')

# system('choco install vim -y')

# system('choco install sysinternals -y')

# system('choco install drawio -y')

# system('choco install gimp -y')

# system('choco install powertoys -y')

# system('choco install googledrive -y')

# system('choco install vlc -y')

# system('choco install gsudo -y') 