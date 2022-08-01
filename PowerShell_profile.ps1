### Enable Oh-My-Posh ###
oh-my-posh init pwsh --config "C:\Users\ryan\Documents\WindowsPowerShell\Theme.omp.json" | Invoke-Expression

### ALIAS ###
# RDP Alias
function rdp([string]$H)
{
     mstsc /v $H
}

# VNC Alias


