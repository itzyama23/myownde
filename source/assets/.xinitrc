#!/bin/sh

# Import bash profile and variables
[ -f ~/.bash_profile ] && . ~/.bash_profile
export user_home="/home/$(whoami)"
export wallpaperDir="$user_home/Pictures/wallpapers"
export wallpaper="arch_linux.png"

# Setup nitrogen
exec nitrogen --set-auto "$wallpaperDir/$wallpaper" --save &
exec openbox-session &
exec reboot
