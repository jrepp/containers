#!/bin/bash
# from: https://askubuntu.com/questions/430853/how-do-i-find-my-internal-ip-address/604691#604691
ip route get 8.8.8.8 | awk '{print $NF; exit}' 
