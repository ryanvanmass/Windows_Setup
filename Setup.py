### Library's ###
from os import system
from os import mkdir
from os import makedirs
from os import path
from os import remove
from os import listdir
from urllib import request
from shutil import unpack_archive
from shutil import copy

### Import Additional Scripts ###
import InstallFont

### Welcome Message ###
print(r"""
 _      _____ _     ____  ____  _      _____
/ \  /|/  __// \   /   _\/  _ \/ \__/|/  __/
| |  |||  \  | |   |  /  | / \|| |\/|||  \  
| |/\|||  /_ | |_/\|  \_ | \_/|| |  |||  /_ 
\_/  \|\____\\____/\____/\____/\_/  \|\____\
                                            
""")

### Configure Terminal and Prompt ###
## Set up Drop Down Terminal ##
# system('powershell.exe Invoke-Webrequest "https://edmi.app/index.php/s/Fg2Z9iDQ9wak5Pz/download/terminal.ico" -Outfile "C:\\Users\\ryan\\Pictures\\terminal.ico"')
# request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/7j3AysGHsdfXLMr/download/Dropdown%20Terminal.lnk', '/Users/ryan/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Windows PowerShell/Dropdown Terminal.lnk')

# Font Install
system('powershell.exe Invoke-Webrequest "https://edmi.app/index.php/s/qnyGqr6Zxykgs9Q/download/fonts.zip" -Outfile "C:\\Users\\ryan\\Downloads\\fonts.zip"')
unpack_archive('/Users/ryan/Downloads/fonts.zip','/Users/ryan/Downloads/fonts')

remove('/Users/ryan/Downloads/fonts/license')
remove('/Users/ryan/Downloads/fonts/readme.md')

FontFolder = listdir('/Users/ryan/Downloads/fonts')
for i in range(len(FontFolder)):
	temp = "/Users/ryan/Downloads/fonts/" + FontFolder[i]
	InstallFont.install_font(temp)

## Configure Windows Terminal ##
if not path.exists('/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState'):
    makedirs('/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState')
    system('choco install microsoft-windows-terminal -y')

if not path.exists("/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"):
    system('powershell.exe Invoke-Webrequest "https://edmi.ap`p/index.php/s/MQn4Gb6YarTrX5k/download/settings.json" -Outfile "C:\\Users\\ryan\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json"')
else:
    remove("/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json")
    system('powershell.exe Invoke-Webrequest "https://edmi.app/index.php/s/MQn4Gb6YarTrX5k/download/settings.json" -Outfile "C:\\Users\\ryan\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json"')



### Install Software ###
## 9P7KNL5RWT25 = Sysinternals
Packages = ["putty.putty", "winscp.winscp", "Famatech.AdvancedIPScanner", "git.git", "vim.vim", "JGraph.draw", "Microsoft.PowerToys", "videolan.vlc", "Google.chrome", "Rufus.Rufus", "xpipe-io.xpipe", "joplin.joplin", "tailscale.tailscale", "nextcloud.nextclouddesktop", "JanDeDobbeleer.OhMyPosh", "Romanitho.Winget-AutoUpdate", "ONLYOFFICE.DesktopEditors", "AutoHotkey.AutoHotkey", "Apple.iTunes"]

for i in range(len(Packages)):
   temp = "winget install " + Packages[i] + " --accept-package-agreements --accept-source-agreements"
   system(temp)

system("winget install Microsoft.VisualStudioCode --override \"/verysilent /suppressmsgboxes /mergetasks='!runcode,addcontextmenufiles,addcontextmenufolders,associatewithfiles,addtopath'\"")


## Choco Testing

# Packages = ["putty", "winscp", "advanced-ip-scanner", "git", "vscode", "vim", "drawio", "PowerToys", "vlc", "tailscale", "onlyoffice", "nextcloud-client", "rufus", "Vivaldi", "xpipe"]
# 
# for i in range(len(Packages)):
#     temp = "choco install " + Packages[i] + " -y"
#     system(temp)
# 
# system("winget install 9P7KNL5RWT25 --accept-package-agreements")


# Enable NFS Support
# system("Enable-WindowsOptionalFeature -FeatureName ClientForNFS-Infrastructure -Online -All")

# Install Clickpaste
request.urlretrieve('https://github.com/Collective-Software/ClickPaste/releases/download/v1.3.0/ClickPaste_v1.3.0.zip', '/Users/ryan/Downloads/ClickPaste.zip')
unpack_archive('/Users/ryan/Downloads/Clickpaste.zip','/Program Files/ClickPaste/')
system("powershell.exe Invoke-Webrequest 'https://edmi.app/index.php/s/Mxp4Yrtt3EtwYiG/download/ClickPaste.exe.lnk' -Outfile 'C:\\Users\\ryan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ClickPaste.exe.lnk'")


# Install MremoteNG
# request.urlretrieve('https://github.com/mRemoteNG/mRemoteNG/releases/download/2023.03.03-v1.77.3-nb/mRemoteNG-Installer-1.77.3.nb-1784.msi, /Users/ryan/Download/mRemoteNG.msi')
# system("/Users/ryan/Download/mRemoteNG.msi /quiet")



## Configure Powershell Prompt ##
# Install Oh-My-Posh
if not path.exists('/Users/ryan/Documents/WindowsPowerShell/'):
    mkdir ('/Users/ryan/Documents/WindowsPowerShell/')
system('Powershell.exe Invoke-Webrequest "https://edmi.app/index.php/s/28KsttE3yPdaBSs/download/Theme.omp.json" -Outfile "C:\\Users\\ryan\\Documents\\WindowsPowerShell\\Theme.omp.json"')

system('choco install oh-my-posh -y')

system('powershell -command "Set-ExecutionPolicy Unrestricted')

# Configure Powershell Profile
request.urlretrieve('https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/main/PowerShell_profile.ps1', '/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1')

### Enable Optional Features ###
## Windows Sandbox ##
system('dism /online /Enable-Feature /FeatureName:"Containers-DisposableClientVM" -All')

## Windows Subsystem for Linux ##
system('dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart')