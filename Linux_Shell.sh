#!/bin/bash
# Download Oh-My-Posh
sudo wget -no-check-certificate https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
sudo chmod +x /usr/local/bin/oh-my-posh

# Download Theme
wget http://edmi.vanmassenhoven.com/index.php/s/aNncBdbZf8fzmDc/download/Theme.omp.json -O /home/ryan/Theme.omp.json
chown ryan /home/ryan/Theme.omp.json

echo 'eval "$(oh-my-posh init bash --config ~/Theme.omp.json)"' >> /home/ryan/.bashrc