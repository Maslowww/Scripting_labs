#!/bin/bash
# ex1
echo "alias myip='ip -4 addr show | grep -oP \"(?<=inet\\s)\\d+(\\.\\d+){3}\"'" >> ~/.bashrc
. ~/.bashrc
myip
