import time
import sys
import random
from colorama import Fore, init

init(autoreset=True)

# Configuration
TARGETS = ["ZESCO_MAIN_GRID", "ZED_BANK_SQL", "ROBLOX_API_V2", "NASA_DEEP_SPACE"]
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
CYAN = Fore.CYAN

def typing_effect(text, color=Fore.WHITE, speed=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def simulate_hack():
    target = random.choice(TARGETS)
    
    # Phase 1: Initiation
    typing_effect(f"[!] INITIALIZING EXPLOIT ON: {target}...", CYAN)
    time.sleep(1)
    
    # Phase 2: The Matrix Scroll
    for _ in range(100):
        # Generate random binary/hex strings
        data = "".join(random.choice("01ABCDEF") for _ in range(40))
        success_chance = random.random()
        
        if success_chance > 0.95:
            print(f"{RED}[!] BYPASSING FIREWALL: {data}")
        else:
            print(f"{GREEN}[+] INJECTING PACKET: {data}")
        
        time.sleep(0.02) # Fast scroll speed

    # Phase 3: Final Access
    print(f"\n{CYAN}----------------------------------------")
    typing_effect("[SUCCESS] ROOT ACCESS GRANTED", GREEN, 0.1)
    typing_effect(f"[DATA] DOWNLOADED 4.2GB FROM {target}", GREEN)
    print(f"{CYAN}----------------------------------------\n")

if __name__ == "__main__":
    try:
        while True:
            simulate_hack()
            cont = input(Fore.YELLOW + "Press ENTER to target next node (or Ctrl+C to exit)... ")
    except KeyboardInterrupt:
        print(f"\n{RED}Hacking Session Terminated.")
