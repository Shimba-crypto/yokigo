import tkinter as tk
from tkinter import messagebox
import hashlib
import webbrowser
import os
import sys
import subprocess

class YokigoSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("YOKIGO v2.0 | PROJECT HUB")
        self.root.geometry("550x450")
        self.root.configure(bg="#050505")
        
        # Security: SHA-224 hash of '777'
        self.master_hash = "af2bdbe1aa9b6ec1e21071da31360e4535458c37d80007b7193ff074"
        
        # Emergency Trigger (Boss Key)
        self.root.bind("<Escape>", lambda e: self.trigger_getaway())
        
        self.boot_security()

    def clear_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- PHASE 1: THE GATE ---
    def boot_security(self):
        self.clear_gui()
        tk.Label(self.root, text="SYSTEM LOCKED", fg="#ff4b2b", bg="#050505", 
                 font=("Courier", 20, "bold")).pack(pady=40)
        
        self.entry = tk.Entry(self.root, show="*", bg="#111", fg="#39ff14", 
                             font=("Courier", 14), insertbackground="#39ff14", 
                             justify="center", relief="flat")
        self.entry.pack(pady=10, ipady=8, padx=60)
        self.entry.focus_set()
        self.entry.bind("<Return>", lambda e: self.verify())

        tk.Button(self.root, text="[ AUTHENTICATE ]", command=self.verify, 
                  bg="#39ff14", fg="black", font=("Courier", 10, "bold"), 
                  relief="flat", width=20).pack(pady=20)

    def verify(self):
        if hashlib.sha224(self.entry.get().encode()).hexdigest() == self.master_hash:
            self.load_dashboard()
        else:
            messagebox.showerror("DENIED", "INCORRECT ACCESS TOKEN")

    # --- PHASE 2: THE HUB ---
    def load_dashboard(self):
        self.clear_gui()
        self.root.geometry("850x550")
        
        # Side Navigation
        nav = tk.Frame(self.root, bg="#111", width=200)
        nav.pack(side="left", fill="y")
        
        tk.Label(nav, text="YOKIGO OS", fg="#00f2ff", bg="#111", 
                 font=("Courier", 14, "bold")).pack(pady=20)

        # Buttons to launch your other scripts
        self.nav_btn(nav, "DASHBOARD", None)
        self.nav_btn(nav, "HACK SIM", lambda: self.run_script("hacked.py"))
        self.nav_btn(nav, "SECURITY", lambda: self.run_script("Yokigo-passes.py"))
        self.nav_btn(nav, "EMERGENCY", self.trigger_getaway)

        # Main Display
        self.display = tk.Frame(self.root, bg="#050505")
        self.display.pack(side="right", expand=True, fill="both", padx=20, pady=20)

        tk.Label(self.display, text=">> WELCOME, SHIMBA", fg="#39ff14", bg="#050505", 
                 font=("Courier", 18)).pack(anchor="w")
        
        # Status Box
        status_box = tk.Text(self.display, bg="#111", fg="white", font=("Courier", 10), 
                             height=15, relief="flat", padx=10, pady=10)
        status_box.pack(fill="x", pady=20)
        status_box.insert("1.0", "[+] System: Operational\n[+] Network: Tunnel Active\n[+] Keybinds: ESC to Purge\n[+] Hub: V2.0 Loaded")
        status_box.config(state="disabled")

    def nav_btn(self, parent, text, cmd):
        tk.Button(parent, text=text, command=cmd, fg="white", bg="#111", 
                  relief="flat", font=("Courier", 10), pady=10, 
                  activebackground="#222").pack(fill="x")

    def run_script(self, script_name):
        """Launches your other Python files in a new process."""
        try:
            subprocess.Popen([sys.executable, script_name])
        except Exception as e:
            messagebox.showerror("Error", f"Could not find {script_name}")

    def trigger_getaway(self):
        """The Boss Key: Instantly runs getaway.py and closes the GUI."""
        try:
            subprocess.Popen([sys.executable, "getaway.py"])
        except:
            webbrowser.open("https://www.google.com/search?q=grade+7+past+papers+zambia")
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = YokigoSystem(root)
    root.mainloop()
