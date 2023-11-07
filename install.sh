#!/bin/sh 

sudo pacman -S - < $(dirname $0)/common/pacman_packages.txt
yay -S - < $(dirname $0)/common/aur_packages.txt

go install github.com/thefryscorer/schemer2@latest
