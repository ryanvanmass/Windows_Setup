### Runtime Variables ###
param (
    $RPORT_URL,
    $RPORT_PORT
)



### Install Chocolatey ### 
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex` ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

### Configure Terminal and Prompt ###
## Set up Drop Down Terminal ##
Invoke-WebRequest http://edmi.vanmassenhoven.com/index.php/s/m2GrjeLPfcfqPrr/download/terminal.ico -OutFile "C:\Users\ryan\Pictures\terminal.ico"
Invoke-WebRequest http://edmi.vanmassenhoven.com/index.php/s/bcrMyjQZg4yDiAH/download/Dropdown%20Terminal.lnk -OutFile "C:\Users\ryan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell\Dropdown Terminal.lnk"

## Configure Powershell Prompt ##
# Install Oh-My-Posh
mkdir C:\Users\ryan\Documents\WindowsPowerShell\
Invoke-WebRequest http://edmi.vanmassenhoven.com/index.php/s/aNncBdbZf8fzmDc/download/Theme.omp.json -OutFile C:\Users\ryan\Documents\WindowsPowerShell\Theme.omp.json
choco install oh-my-posh -y
choco install firacodenf -y
Set-ExecutionPolicy Unrestricted

# Configure Ppowershell Profile
# Write-Output 'oh-my-posh init pwsh --config "C:\Users\ryan\Documents\WindowsPowerShell\Theme.omp.json" | Invoke-Expression' >> C:\Users\ryan\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
Invoke-WebRequest https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/test/PowerShell_profile.ps1 -OutFile C:\Users\ryan\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
Write-Output "# Carrionspike Tailscale Alias" >> C:\Users\ryan\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
Write-Output "$CarrionSpike=${RPORT_URL}:${RPORT_PORT}" >> C:\Users\ryan\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

## Configure Windows Terminal ##
mkdir -p C:\Users\ryan\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState
Invoke-WebRequest http://edmi.vanmassenhoven.com/index.php/s/ywxdD6CFZFDB249/download/settings.json -OutFile C:\Users\ryan\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
choco install microsoft-windows-terminal -y

## WSL Configuration ##
$WSL_Check=Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux | Select -ExpandProperty State # Caches the variable if WSL is enabled or not

if($WSL_Check -eq "Enabled"){
Invoke-WebRequest https://raw.githubusercontent.com/ryanvanmass/Windows_Setup/test/Linux_Shell.sh -Outfile \\wsl$\Ubuntu\home\ryan\Linux_Shell.sh
wsl -u root chmod +x /home/ryan/Linux_Shell.sh
wsl -u root sh /home/ryan/Linux_Shell.sh
}



### Install Software ###
choco install GoogleChrome -y

choco install putty -y

choco install winscp -y

choco install advanced-ipscanner -y

choco install git -y

choco install vscode -y

choco install ringcentral-classic -y --ignore-checksum

choco install vim -y

choco install sysinternals -y

choco install drawio -y

choco install gimp -y

choco install powertoys -y

choco install googledrive -y

choco install vlc -y

choco install gsudo -y
