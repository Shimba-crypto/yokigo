import tkinter as tk
from tkinter import messagebox
import hashlib
import webbrowser
import os
import sys

class YokigoOS:
    def __init__(self, root):
        self.root = root
        self.root.title("YOKIGO v1.8 | NEON WRAITH")
        self.root.geometry("500x400")
        self.root.configure(bg="#050505")
        
        # Security: SHA-224 hash of '777'
        self.master_hash = "af2bdbe1aa9b6ec1e21071da31360e4535458c37d80007b7193ff074"
        
        # Bind the Getaway Protocol (Boss Key) to the Escape key
        self.root.bind("<Escape>", lambda e: self.trigger_getaway())
        
        self.show_auth_gate()

    def clear_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- PHASE 1: SECURITY GATE ---
    def show_auth_gate(self):
        self.clear_ui()
        tk.Label(self.root, text="YOKIGO KERNEL", fg="#00f2ff", bg="#050505", 
                 font=("Courier", 22, "bold")).pack(pady=40)
        
        tk.Label(self.root, text="INPUT CLEARANCE TOKEN", fg="white", bg="#050505", 
                 font=("Courier", 9)).pack()

        self.token_entry = tk.Entry(self.root, show="*", bg="#1a1a1a", fg="#39ff14", 
                                   insertbackground="#39ff14", font=("Courier", 14), 
                                   justify='center', relief="flat")
        self.token_entry.pack(pady=15, ipady=8, padx=50)
        self.token_entry.focus_set()
        
        # Press Enter to authenticate
        self.token_entry.bind("<Return>", lambda e: self.authenticate())

        tk.Button(self.root, text="[ INITIALIZE ]", command=self.authenticate, 
                  bg="#00f2ff", fg="black", font=("Courier", 10, "bold"), 
                  activebackground="#39ff14", relief="flat", width=20).pack(pady=20)

    def authenticate(self):
        token = self.token_entry.get()
        if hashlib.sha224(token.encode()).hexdigest() == self.master_hash:
            self.show_main_hub()
        else:
            messagebox.showerror("SECURITY", "INVALID TOKEN. LOGGED.")
            self.token_entry.delete(0, tk.END)

    # --- PHASE 2: THE HUB ---
    def show_main_hub(self):
        self.clear_ui()
        self.root.geometry("800x500")
        
        # Top Status Bar
        status_bar = tk.Frame(self.root, bg="#1a1a1a", height=30)
        status_bar.pack(fill="x", side="top")
        tk.Label(status_bar, text="STATUS: ENCRYPTED // ESC TO PURGE", fg="#39ff14", 
                 bg="#1a1a1a", font=("Courier", 9)).pack(side="left", padx=10)

        # Main Layout
        content = tk.Frame(self.root, bg="#050505")
        content.pack(expand=True, fill="both", padx=30, pady=30)

        # Left Column: Tools
        tools_frame = tk.LabelFrame(content, text=" PROJECTS ", fg="#00f2ff", bg="#050505", font=("Courier", 10))
        tools_frame.pack(side="left", fill="both", expand=True, padx=10)

        self.add_btn(tools_frame, "ZAZA DEFENDER 4.0", lambda: print("Launching Security..."))
        self.add_btn(tools_frame, "ROBLOX EXPLOIT HUB", lambda: print("Booting Roblox..."))
        self.add_btn(tools_frame, "TERMINAL SIMULATOR", lambda: print("Opening Terminal..."))

        # Right Column: Panic/Getaway
        panic_frame = tk.LabelFrame(content, text=" PROTOCOLS ", fg="#ff4b2b", bg="#050505", font=("Courier", 10))
        panic_frame.pack(side="right", fill="both", expand=True, padx=10)

        self.add_btn(panic_frame, "FORCE PURGE (ESC)", self.trigger_getaway, color="#ff4b2b")
        self.add_btn(panic_frame, "WIPE CACHE", lambda: messagebox.showinfo("Yokigo", "Cache Purged."))

    def add_btn(self, parent, text, cmd, color="#00f2ff"):
        tk.Button(parent, text=text, command=cmd, fg=color, bg="#1a1a1a", 
                  font=("Courier", 10, "bold"), relief="flat", pady=10).pack(fill="x", pady=10, padx=10)

    # --- PHASE 3: GETAWAY (EMERGENCY) ---
    def trigger_getaway(self):
        # Open the decoy site immediately
        webbrowser.open("https://www.google.com/search?q=grade+7+science+past+papers+zambia")
        # Kill the app
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = YokigoOS(root)
    root.mainloop()
