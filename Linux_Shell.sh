#!/bin/bash
sudo wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
wget http://edmi.vanmassenhoven.com/index.php/s/aNncBdbZf8fzmDc/download/Theme.omp.json
sudo chmod +x /usr/local/bin/oh-my-posh

eval "$(oh-my-posh init bash --config ~/Theme.omp.json)"