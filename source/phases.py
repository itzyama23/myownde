import subprocess
from . import log_prefixes

# This loads the prefix logs
prefix = log_prefixes.LogPrefix

def phase0():
    phase1()
    phase2()
    phase3()
    phase4()
    phase5()
    phase6()
    phase7()
    phase8()

def phase1():
    packages=[
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
        "network-manager-applet"
    ]
    print(f"{prefix.INFO.value} Install everything...")
    command = ["sudo", "pacman", "-S", "--noconfirm", "--needed"] + packages
    subprocess.run(command, check="True")
    print(f"{prefix.INFO.value} All the packages were installed!")

def phase2():
    print(f"{prefix.INFO.value} Enabling and configuring essential services...")

def phase3():
    print(f"{prefix.INFO.value} Importing dotfiles...")

def phase4():
    print(f"{prefix.INFO.value} Installing icons...")

def phase5():
    print(f"{prefix.INFO.value} Installing DE background...")

def phase6():
    print(f"{prefix.INFO.value} Installing greeter background and avatar...")

def phase7():
    print(f"{prefix.INFO.value} Installing GRUB theme...")

def phase8():
    print(f"{prefix.INFO.value} Installing Plymouth theme...")