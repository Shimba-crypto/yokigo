import hashlib
import time
import datetime
import os
from colorama import Fore, init

init(autoreset=True)

# 1. Hashed Password (This is '777')
MASTER_HASH = "af2bdbe1aa9b6ec1e21071da31360e4535458c37d80007b7193ff074" 

def log_event(status, user):
    """3. Login Logging"""
    with open("security_logs.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] User: {user} | Status: {status}\n")

def check_pc_identity():
    """8. System ID Check"""
    # Only allows the script to run if the PC name matches yours
    # Replace 'YOUR_PC_NAME' with your actual computer name
    return os.environ.get('COMPUTERNAME') == 'YOUR_PC_NAME'

def verify_gate():
    attempts = 0
    while attempts < 3:
        print(Fore.CYAN + f"\n[ YOKIGO SECURITY ATTEMPT {attempts + 1}/3 ]")
        user_input = input(Fore.WHITE + "ENTER ACCESS TOKEN: ")
        
        # 1. Hash the input to compare
        input_hash = hashlib.sha224(user_input.encode()).hexdigest()

        if input_hash == MASTER_HASH:
            print(Fore.GREEN + "\n[+] IDENTITY CONFIRMED. BOOTING KERNEL...")
            log_event("SUCCESS", "Admin")
            return True
        else:
            attempts += 1
            # 2. Anti-Brute Force delay
            wait_time = attempts * 2
            print(Fore.RED + f"[!] ACCESS DENIED. LOCKING FOR {wait_time}s...")
            log_event("FAILED", "Unknown")
            time.sleep(wait_time)

    # 4. Auto-Lockdown
    print(Fore.RED + "\n[!!!] MAXIMUM ATTEMPTS EXCEEDED. SYSTEM FROZEN.")
    return False

if __name__ == "__main__":
    if verify_gate():
        print(Fore.CYAN + "Welcome back, Shimba.")
