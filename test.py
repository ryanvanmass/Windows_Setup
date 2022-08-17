# X = ["0","1","2"]

# for i in range(len(X)):
#     print(X[i])

################################################################################################
from os import system

Packages = ["GoogleChrome", "putty", "winscp", "advanced-ipscanner", "git", "vscode", "vim", "sysinternals", "drawio", "gimp", "powertoys", "googledrive", "vlc", "gsudo"]

for i in range(len(Packages)):
    system("choco install ", Packages[i], " -y")




### Install Software ###
# system('choco install ringcentral-classic -y --ignore-checksum')