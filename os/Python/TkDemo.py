import tkinter as tk

# --- 1. INFO.REDIRECT PARSING LOGIC ---
def verify_credentials_from_disk():
    target_user = ""
    target_pass = ""
    
    # Safely target your consolidated Info.redirect file
    with open("os/TerminalShells/SyS/binary/Info.redirect", "r") as file:
        for line in file:
            cleaned_line = line.strip()
            
            # Identify the key assignment line
            if "==" in cleaned_line:
                key, value = cleaned_line.split("==", 1)
                key = key.strip()
                
                # Strip out the quotation marks surrounding your values
                value = value.strip().replace('"', '')
                
                if key == "user":
                    target_user = value
                elif key == "pass":
                    target_pass = value
                    
    return target_user, target_pass

# --- 2. AUTHENTICATION ACTION ---
def check_login():
    entered_username = username_input.get()
    entered_password = password_input.get()
    
    # Grab the exact strings dynamically from Info.redirect
    correct_user, correct_pass = verify_credentials_from_disk()
    
    if entered_username == correct_user and entered_password == correct_pass:
        status_label.config(text="Access Granted! Booting VibeOS...", fg="green")
        # [Your next screen transition will drop here]
    else:
        status_label.config(text="Invalid Credentials. Try again.", fg="red")

# --- 3. WINDOW INITIALIZATION ---
root = tk.Tk()
root.title("VibeOS Secure Login")
root.geometry("350x250")
root.configure(bg="#0d1117")

# --- 4. WIDGET DEPLOYMENT ---
title_label = tk.Label(root, text="VibeOS Auth Node", font=("sans-serif", 14, "bold"), bg="#0d1117", fg="#58a6ff")
title_label.pack(pady=15)

username_label = tk.Label(root, text="Username:", font=("sans-serif", 10), bg="#0d1117", fg="#c9d1d9")
username_label.pack()
username_input = tk.Entry(root, font=("sans-serif", 10), width=25)
username_input.pack(pady=5)

password_label = tk.Label(root, text="Password:", font=("sans-serif", 10), bg="#0d1117", fg="#c9d1d9")
password_label.pack()
password_input = tk.Entry(root, show="*", font=("sans-serif", 10), width=25)
password_input.pack(pady=5)

login_button = tk.Button(root, text="Login", font=("sans-serif", 10, "bold"), width=12, command=check_login)
login_button.pack(pady=15)

status_label = tk.Label(root, text="", font=("sans-serif", 9), bg="#0d1117")
status_label.pack()

# --- 5. RUN ENGINE ---
root.mainloop()
