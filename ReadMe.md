# Install
**NOTE:** Must be run as an administrator
1. Download most recent release
2. Unzip Archive
3. Run the following commands
```
	Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
	choco install python

	# Relaunch Terminal
	python Setup.py
```
