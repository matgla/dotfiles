#!/bin/bash

killall swww-daemon 

swww-daemon &
sleep 0.5 
export GOPATH=$HOME/go 
export PATH=$PATH:$GOPATH/bin
 
$HOME/.config/wallpaper/wallpaper_change.py -i $WALLPAPERS_PATH
