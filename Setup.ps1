### Global Variables ###
# Set the path to the folder containing the fonts
$fontFolderPath = "C:\Users\ryan\Downloads\fonts"




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
Invoke-Webrequest "https://edmi.app/index.php/s/qnyGqr6Zxykgs9Q/download/fonts.zip" -Outfile C:\Users\ryan\Downloads\fonts.zip
Expand-Archive -LiteralPath C:\Users\ryan\Downloads\fonts.zip -DestinationPath C:\Users\ryan\fonts

# Call the function to install the fonts
Install-FontsInFolder -folderPath $fontFolderPath

## Configure Windows Terminal
Invoke-Webrequest "https://edmi.app/index.php/s/MQn4Gb6YarTrX5k/download/settings.json" -Outfile C:\Users\ryan\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json

