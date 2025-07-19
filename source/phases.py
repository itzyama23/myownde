import subprocess

def phase0():
    packages=(
        "noto-fonts",
        "noto-fonts-cjk",
        "git",
        "curl",
        "nano",
        "tmux",
        "xpdf",
        "xterm",
        "pavucontrol",
        "rofi",
        "htop",
        "fastfetch",
        "pcmanfm",
        "gvfs",
        "firefox",
        "keepassxc",
        "flatpak",
        "openbox",
        "obconf-qt",
        "tint2",
        "nitrogen",
        "volumeicon",
        "brightnessctl",
        "lightdm",
        "lightdm-gtk-greeter",
        "plymouth",
    )
    print("[INFO] Install everything...")
    args=""
    for package in packages:
        args+=f"{package} "
    subprocess(["sudo", "pacman", "-S", args], shell=True)   

def phase1():
    print("[INFO] Install installation...")

def phase2():
    print("[INFO] Enabling and configuring essential services...")

def phase3():
    print("[INFO] Importing dotfiles...")

def phase4():
    print("[INFO] Installing icons...")

def phase5():
    print("[INFO] Installing DE background...")

def phase6():
    print("[INFO] Installing greeter background and avatar...")

def phase7():
    print("[INFO] Installing GRUB theme...")

def phase8():
    print("[INFO] Installing Plymouth theme...")