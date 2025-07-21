import subprocess
from pathlib import Path
from . import log_prefixes
from . import libphases


# This loads the prefix logs
prefix = log_prefixes.LogPrefix
currentDir = Path.cwd()

user = subprocess.run(["whoami"], capture_output=True, text=True).stdout.replace("\n", "")
home = f"/home/{user}"
config = f"{home}/.config"
globalShare = "/usr/share"

# Routes to be copied
iconsTheme = f"{currentDir}/source/assets/oxylite-icon-theme"

# Config routes
openbox = f"{config}/openbox"
tint2 = f"{config}/tint2"
scripts = f"{config}/scripts"
iconsRoute = f"{globalShare}/icons"

routes = [
    openbox,
    tint2,
    scripts
]

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
    
    # Refreshing repo and updating packages
    print(f"{prefix.INFO.value} Updating packages if needed...")
    subprocess.run(["sudo", "pacman", "-Syyu", "--noconfirm"])
    print(f"{prefix.SUCCESS.value} Packages were updated succesfully!")

    # Installing all the packages needed
    print(f"{prefix.INFO.value} Install everything...")
    command = ["sudo", "pacman", "-S", "--noconfirm", "--needed"] + packages
    subprocess.run(command, check="True")
    print(f"{prefix.INFO.value} All the packages were installed!")

def phase2():
    print(f"{prefix.INFO.value} Enabling and configuring essential services...")
    
    # Enable lightdm
    subprocess.run(["sudo", "systemctl", "enable", "lightdm"])
    print(f"{prefix.INFO.value} lightdm service was enabled!")

    # Added user to lightdm group
    subprocess.run(["sudo", "usermod", "-aG", "lightdm", user])
    print(f"{prefix.INFO.value} The user: {user} was added to lightdm group!")
    
    # Change home permisions to: rwx|r-x|r-x
    subprocess.run(["chmod", "755", home])
    print(f"{prefix.SUCCESS.value} Home directory permissions were changed successfully!")
    print(f"{prefix.INFO.value} New permssions for: {home} are: rwx|r-x|r-x")

def phase3():
    print(f"{prefix.INFO.value} Importing dotfiles...")
    
    for route in routes:
        if not (libphases.checkDirectory(route)):
            print(f"{prefix.INFO.value} Creating: {route}")
            libphases.createDirectory(route)
            print(f"{prefix.SUCCESS.value} {route} was created!")
        else:
            print(f"{prefix.INFO.value} {route} already exists...")

def phase4():
    print(f"{prefix.INFO.value} Installing icons...")
    libphases.copyFilesFrom(iconsTheme, iconsRoute, sudo=True)
    print(f"{prefix.SUCCESS.value} Icons were installed sucessfully!")

def phase5():
    print(f"{prefix.INFO.value} Installing DE background...")

def phase6():
    print(f"{prefix.INFO.value} Installing greeter background and avatar...")

def phase7():
    print(f"{prefix.INFO.value} Installing GRUB theme...")

def phase8():
    print(f"{prefix.INFO.value} Installing Plymouth theme...")