from source import phases

def main():
    # Header
    with open('header.txt', encoding="utf-8") as file:
        header = file.read()
        print(header)
    
    print("\nChoose an option: ")
    print("""
          0. Install everything
          1. Package installation
          2. Enable and configure essential services
          3. Import dotfiles
          4. Install icons
          5. Install DE background
          6. Install greeter background and avatar
          7. Install GRUB theme
          8. Install Plymouth theme
          x (or Ctrl+D). Exit  
        """)
    
    option = input("> ")
    
    # Checks if you're using a valid option
    if option.isdigit() and 0 <= int(option) <= 8:
        getattr(phases, f"phase{option}")()
    elif option == "x":
        print("Exit sucessfully...")
    else:
        print("Not a valid option...")

main()