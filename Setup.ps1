# Install Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Set up Drop Down Terminal
Invoke-WebRequest http://edmi.vanmassenhoven.com/index.php/s/m2GrjeLPfcfqPrr/download/terminal.ico -OutFile "C:\Users\ryan\Pictures\terminal.ico"
Invoke-WebRequest http://edmi.vanmassenhoven.com/index.php/s/ypT9jtdePX5dyep/download/Dropdown%20Terminal.lnk -OutFile "C:\Users\ryan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell\Dropdown Terminal.lnk"


# Install Software
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
