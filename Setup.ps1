### Global Variables ###
# Set the path to the folder containing the fonts
$fontFolderPath = "C:\Users\ryan\Downloads\fonts"

$Packages = @("putty.putty", "winscp.winscp", "Famatech.AdvancedIPScanner", "git.git", "vim.vim", "JGraph.draw", "Microsoft.PowerToys", "videolan.vlc", "Google.chrome", "Rufus.Rufus", "xpipe-io.xpipe", "joplin.joplin", "tailscale.tailscale", "nextcloud.nextclouddesktop", "JanDeDobbeleer.OhMyPosh", "Romanitho.Winget-AutoUpdate", "ONLYOFFICE.DesktopEditors", "AutoHotkey.AutoHotkey", "Apple.iTunes")

$User_DIR = "$User_Dir"


### Functions ###
## Install Fonts ##
function Install-Font {
    param(
        [string]$fontPath
    )

    $shell = New-Object -ComObject Shell.Application
    $folder = $shell.Namespace(0x14)
    $folder.CopyHere($fontPath)
}

function Install-FontsInFolder {
    param(
        [string]$folderPath
    )

    Get-ChildItem -Path $folderPath -Recurse -File -Include *.ttf,*.otf,*.woff,*.eot,*.woff2 | ForEach-Object {
        Install-Font -fontPath $_.FullName
    }
}

### Configure Prompt ###
## Import Font ##
Invoke-Webrequest "https://edmi.app/index.php/s/qnyGqr6Zxykgs9Q/download/fonts.zip" -Outfile "$User_Dir\Downloads\fonts.zip"
Expand-Archive -LiteralPath $User_Dir\Downloads\fonts.zip -DestinationPath $User_Dir\fonts

# Call the function to install the fonts
Install-FontsInFolder -folderPath $fontFolderPath

## Configure Windows Terminal ##
Invoke-Webrequest "https://edmi.app/index.php/s/MQn4Gb6YarTrX5k/download/settings.json" -Outfile "$User_Dir\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings."json

## Powerhsell Profile Config ##
Invoke-Webreqeust "https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/main/PowerShell_profile.ps1" -Outfile "$User_Dir\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1"

### Package Install ###
Get-ChildItem $Packages | ForEach-Object {
    winget install $_ --accept-package-agreements --accept-source-agreements
}

# Install VS Code
winget install Microsoft.VisualStudioCode --override "/verysilent /suppressmsgboxes /mergetasks='!runcode,addcontextmenufiles,addcontextmenufolders,associatewithfiles,addtopath'"

# Install Clickpaste
Invoke-WebRequest "https://github.com/Collective-Software/ClickPaste/releases/download/v1.3.0/ClickPaste_v1.3.0.zip" -OutFile "$User_Dir\Downloads\ClickPaste.zip"
Invoke-Webrequest 'https://edmi.app/index.php/s/Mxp4Yrtt3EtwYiG/download/ClickPaste.exe.lnk' -Outfile '$User_Dir\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ClickPaste.exe.lnk'

## Optioanl Feature Install ##
# Windows Sandbox
dism /online /Enable-Feature /FeatureName:"Containers-DisposableClientVM" -All

## WSL
dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart