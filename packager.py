import os
import subprocess
import sys
from colorama import Fore, init

init(autoreset=True)

def build_exe():
    print(Fore.CYAN + "========================================")
    print(Fore.CYAN + "       YOKIGO COMPILER PROTOCOL         ")
    print(Fore.CYAN + "========================================\n")

    # 1. Configuration
    script_to_build = "main_gui.py"
    app_name = "Yokigo_OS"
    icon_file = "yokigo.ico" # Make sure this exists in your folder!
    
    if not os.path.exists(script_to_build):
        print(Fore.RED + f"[!] ERROR: {script_to_build} not found.")
        return

    # 2. Command Construction
    # --onefile: Everything in one EXE
    # --noconsole: No black terminal box
    # --clean: Clear temporary cache before building
    cmd = [
        "pyinstaller",
        "--noconsole",
        "--onefile",
        f"--name={app_name}",
        f"--icon={icon_file}" if os.path.exists(icon_file) else "",
        "--clean",
        script_to_build
    ]

    # Remove empty strings if icon doesn't exist
    cmd = [arg for arg in cmd if arg]

    print(Fore.YELLOW + f"[*] STARTING BUILD: {app_name}...")
    print(Fore.WHITE + "This may take a minute depending on your system...\n")

    try:
        # Execute PyInstaller
        subprocess.check_call(cmd)
        
        print(Fore.GREEN + "\n========================================")
        print(Fore.GREEN + f"[SUCCESS] {app_name}.exe generated in /dist")
        print(Fore.GREEN + "========================================")
        
    except subprocess.CalledProcessError:
        print(Fore.RED + "\n[!] ERROR: Build failed. Ensure PyInstaller is installed.")
        print(Fore.YELLOW + "Try: pip install pyinstaller")
    except Exception as e:
        print(Fore.RED + f"\n[!] UNKNOWN ERROR: {e}")

if __name__ == "__main__":
    build_exe()
