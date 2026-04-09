import os
import subprocess
import webbrowser
import time
from colorama import Fore, init

init(autoreset=True)

def activate_getaway():
    print(Fore.RED + "[!!!] GETAWAY PROTOCOL ACTIVATED")
    
    # 1. Open the Decoy Site (Grade 7 Revision or Google)
    # This makes it look like you are just studying.
    decoy_url = "https://www.google.com/search?q=grade+7+past+papers+zambia"
    webbrowser.open(decoy_url)

    # 2. Attempt to close the main Yokigo GUI if it's running
    # This works on Windows. For Mac/Linux, use 'pkill -f'
    try:
        if os.name == 'nt':
            os.system('taskkill /F /IM python.exe /T')
        else:
            os.system('pkill -f python')
    except:
        pass

    # 3. Clear the screen immediately
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("System Cleaned.")

if __name__ == "__main__":
    # In a full project, you could trigger this by a specific keypress 
    # or by running this script from a shortcut.
    activate_getaway()
