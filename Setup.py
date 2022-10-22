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

### Configure Terminal and Prompt ###
## Set up Drop Down Terminal ##
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/m2GrjeLPfcfqPrr/download/terminal.ico','/Users/ryan/Pictures/terminal.ico')
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/bcrMyjQZg4yDiAH/download/Dropdown%20Terminal.lnk', '/Users/ryan/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Windows PowerShell/Dropdown Terminal.lnk')


## Configure Powershell Prompt ##
# Install Oh-My-Posh
if not path.exists('/Users/ryan/Documents/WindowsPowerShell/'):
    mkdir ('/Users/ryan/Documents/WindowsPowerShell/')
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/aNncBdbZf8fzmDc/download/Theme.omp.json', '/Users/ryan/Documents/WindowsPowerShell/Theme.omp.json')

system('winget install JanDeDobbeleer.ohmyposh --accept-package-agreements')

system('powershell -command "Set-ExecutionPolicy Unrestricted')


# Font Install
request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/baotyKMF6w2D6Cp/download/fonts.zip', '/Users/ryan/Downloads/fonts.zip')
unpack_archive('/Users/ryan/Downloads/fonts.zip','/Users/ryan/Downloads/fonts')

remove('/Users/ryan/Downloads/fonts/license')
remove('/Users/ryan/Downloads/fonts/readme.md')

FontFolder = listdir('/Users/ryan/Downloads/fonts')
for i in range(len(FontFolder)):
	temp = "/Users/ryan/Downloads/fonts/" + FontFolder[i]
	InstallFont.install_font(temp)



# Configure Ppowershell Profile
request.urlretrieve('https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/main/PowerShell_profile.ps1', '/Users/ryan/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1')


## Configure Windows Terminal ##
if not path.exists('/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState'):
    makedirs('/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState')
    system('winget install Microsoft.WindowsTerminal --accept-package-agreements')

if not path.exists("/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"):
    request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/ywxdD6CFZFDB249/download/settings.json', '/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json')
else:
    remove("/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json")
    request.urlretrieve('http://edmi.vanmassenhoven.com/index.php/s/ywxdD6CFZFDB249/download/settings.json', '/Users/ryan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json')



### Install Software ###
## 9P7KNL5RWT25 = Sysinternals
Packages = ["Google.Chrome", "putty.putty", "winscp.winscp", "Famatech.AdvancedIPScanner", "git.git", "Microsoft.VisualStudioCode", "vim.vim", "9P7KNL5RWT25", "JGraph.draw", "Microsoft.PowerToys", "google.drive", "videolan.vlc", "gerardog.gsudo", "TeamViewer.TeamViewer"]

for i in range(len(Packages)):
    temp = "winget install " + Packages[i] + " --accept-package-agreements"
    system(temp)

system('winget install RingCentral.RingCentral --accept-package-agreements --ignore-checksum')
