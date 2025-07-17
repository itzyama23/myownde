#!/bin/bash

# THIS AWFUL SCRIPT IS MEANT TO BE USED ALONGSIDE ARCHINSTALL SCRIPT,
# GIVE MORE TIME, I SWEAR I'LL BE ABLE TO MAKE IT AVAILABLE FOR A CUSTOM CONFIG FR
# IF YOU'RE GONNA FORK IT AND PUBLISH A MOD OF THIS(THESE) SCRIPT(S), AT LEAST
# GIVE CREDITS PLS. I'D REALLY APPREACIATE IT!

# Install tools (i don't even know if these are good practices, but whatever...)
# noto-fonts-cjk noto-fonts ( Japanese fonts (yes, Im an otaku, so what? )
# git curl nano tmux # Emergency Tools
# xpdf xterm pavucontrol rofi htop fastfetch pcmanfm gvfs firefox keepassxc flatpak ( Applications I'd be using )
# openbox obconf tint2 nitrogen ( Desktop Environment stuff )
# volumeicon brightnessctl ( Additional stuff for my DE )
# lightdm lightdm-gtk-greeter plymouth ( Greeter and splash screen before greeter )

# PHASE 1: Installation of the packages I use
set -e

PKGS=(
    noto-fonts
    noto-fonts-cjk
    git
    curl
    nano
    tmux
    xpdf
    xterm
    pavucontrol
    rofi
    htop
    fastfetch
    pcmanfm
    gvfs
    firefox
    keepassxc
    flatpak
    openbox
    obconf-qt
    tint2
    nitrogen
    volumeicon
    brightnessctl
    lightdm
    lightdm-gtk-greeter
    plymouth
)

echo "< ====================== >"
echo "WARNING: DO NOT USE SUDO, DO NOT RUN AS ROOT!!!"
echo "You're running this script as: $(whoami)"
echo ""
echo "< ====================== >"

echo "[INFO] ---> Installing all the necessary packages..."  
sudo pacman -Syu --noconfirm
sudo pacman -S --noconfirm --needed "${PKGS[@]}"
echo "[OK] Paquetes instalados con éxito"

# PHASE 2: Enable essential services
sudo systemctl enable lightdm
sudo usermod -aG lightdm "$(whoami)"
chmod 755 $HOME

# PHASE 3: IMPORT DOTFILES!!!
user_home="$HOME"
openbox="$user_home/.config/openbox"
tint2="$user_home/.config/tint2"
scripts="$user_home/.config/scripts"

function checkDirectory() {
    if [ ! -d "$1" ]; then
        echo "[INFO] Directory '$1' couldn't be found"
        echo "Creating directory: '$1'"

        if [ $2 = "true"  ]; then
            sudo mkdir -p $1
        else
            mkdir -p $1
        fi
    fi
}

# Check if these directories don't exist, if not,
# then it will create them.
checkDirectory $openbox "false"
checkDirectory $tint2 "false"
checkDirectory $scripts "false"

# Copy all my settings for OpenBox
# PHASE 3: IMPORT DOTFILES!!!
function copySettings() {
    echo "<===== READING FOLDER: $1 =====>"
    for file in "$(pwd)"/$1/*; do
        if [[ -f "$file" ]]; then
            echo "Processing file: $file"
            cp $file $2
            echo "$file was copied successfully!"
        fi
    done
}

copySettings "openbox" $openbox
copySettings "tint2" $tint2
copySettings "scripts" $scripts

# PHASE 4: Setting up visuals
wallpaperDir_DE="$user_home/Pictures/wallpapers"
wallpaper_DE="arch_linux.png"
wallpaperDir_lightdm="/usr/share/backgrounds"
wallpaper_lightdm="nekopara.png"
user_avatar=".face"

# DE Implementation
checkDirectory $wallpaperDir_DE "false"
cp "$(pwd)/$wallpaper_DE" "$wallpaperDir_DE"

# Greeter Implementation
checkDirectory $wallpaperDir_lightdm "true"
sudo cp "$(pwd)/$wallpaper_lightdm" "$wallpaperDir_lightdm"

# Avatar Implementation
checkDirectory $user_avatar "false"
cp "$(pwd)/$user_avatar" "$user_home"

# Install wallpaper
cp "$(pwd)/.xinitrc" "$user_home/"
chmod +x "$user_home/.xinitrc"
touch "$user_home/.Xauthority"
startx
