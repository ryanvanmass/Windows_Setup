### ALIAS ###
# RDP Alias
function rdp([string]$H)
{
     mstsc /v $H
}

function uptime {
        Get-WmiObject win32_operatingsystem | select csname, @{LABEL='LastBootUpTime';
        EXPRESSION={$_.ConverttoDateTime($_.lastbootuptime)}}
}

function df {
        get-volume
}




### Enable Oh-My-Posh ###
oh-my-posh init pwsh --config "C:\Users\ryan.rdvm\Documents\WindowsPowerShell\Theme.omp.json" | Invoke-Expression
