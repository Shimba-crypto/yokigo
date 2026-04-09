import tkinter as tk
from tkinter import messagebox
import hashlib
import time

class YokigoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YOKIGO | SECURE TERMINAL")
        self.root.geometry("500x350")
        self.root.configure(bg="#050505")
        
        # Security Config (SHA-224 hash for '777')
        self.master_hash = "af2bdbe1aa9b6ec1e21071da31360e4535458c37d80007b7193ff074"
        self.attempts = 0

        self.show_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- SCREEN 1: THE GATE ---
    def show_login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="[ YOKIGO SECURITY GATE ]", fg="#00f2ff", bg="#050505", 
                 font=("Courier", 18, "bold")).pack(pady=30)

        tk.Label(self.root, text="ENTER ACCESS TOKEN:", fg="white", bg="#050505", 
                 font=("Courier", 10)).pack()

        self.pass_entry = tk.Entry(self.root, show="*", bg="#1a1a1a", fg="#39ff14", 
                                   insertbackground="white", font=("Courier", 14), justify='center')
        self.pass_entry.pack(pady=10, ipady=5)
        self.pass_entry.bind("<Return>", lambda e: self.verify_token())

        tk.Button(self.root, text="AUTHENTICATE", command=self.verify_token, 
                  bg="#00f2ff", fg="black", font=("Courier", 10, "bold"), 
                  relief="flat", width=20).pack(pady=20)

    def verify_token(self):
        entered = self.pass_entry.get()
        hashed_attempt = hashlib.sha224(entered.encode()).hexdigest()

        if hashed_attempt == self.master_hash:
            self.show_dashboard()
        else:
            self.attempts += 1
            if self.attempts >= 3:
                messagebox.showerror("CRITICAL", "SYSTEM LOCKDOWN INITIATED")
                self.root.destroy()
            else:
                messagebox.showwarning("DENIED", f"INVALID TOKEN ({self.attempts}/3)")
                self.pass_entry.delete(0, tk.END)

    # --- SCREEN 2: THE DASHBOARD ---
    def show_dashboard(self):
        self.clear_screen()
        self.root.geometry("700x450")
        
        # Header
        header = tk.Frame(self.root, bg="#00f2ff", height=50)
        header.pack(fill="x")
        tk.Label(header, text="YOKIGO COMMAND CENTER v1.5", fg="black", bg="#00f2ff", 
                 font=("Courier", 14, "bold")).pack(pady=10)

        # Content Area
        main_frame = tk.Frame(self.root, bg="#050505")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Status Panel
        status_box = tk.LabelFrame(main_frame, text=" SYSTEM STATUS ", fg="#39ff14", 
                                   bg="#050505", font=("Courier", 10), padx=10, pady=10)
        status_box.pack(side="left", fill="both", expand=True)
        
        stats = ["ENCRYPTION: ACTIVE", "NETWORK: HIDDEN", "KERNEL: STABLE", "USER: SHIMBA"]
        for s in stats:
            tk.Label(status_box, text=f"> {s}", fg="white", bg="#050505", 
                     font=("Courier", 11)).pack(anchor="w", pady=2)

        # Action Panel
        btn_frame = tk.Frame(main_frame, bg="#050505")
        btn_frame.pack(side="right", fill="both", expand=True, padx=20)

        self.create_neon_btn(btn_frame, "LAUNCH ROBLOX HUB", "#00f2ff")
        self.create_neon_btn(btn_frame, "ZAZA DEFENDER", "#39ff14")
        self.create_neon_btn(btn_frame, "WIPE SESSION LOGS", "#ff4b2b")

    def create_neon_btn(self, parent, text, color):
        tk.Button(parent, text=text, fg=color, bg="#1a1a1a", relief="flat", 
                  font=("Courier", 10, "bold"), height=2, pady=5).pack(fill="x", pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = YokigoApp(root)
    root.mainloop()
