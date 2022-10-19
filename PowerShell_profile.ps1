### ALIAS ###
# RDP Alias
function rdp([string]$H)
{
     mstsc /v $H
}








### Enable Oh-My-Posh ###
oh-my-posh init pwsh --config "C:\Users\ryan.rdvm\Documents\WindowsPowerShell\Theme.omp.json" | Invoke-Expression
