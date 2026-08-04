import tkinter as tk

# --- 1. FILE READ & PARSING LOGIC ---
def verify_credentials_from_disk():
    target_user = ""
    target_pass = ""
    
    # Reads your local configuration file line-by-line
    # Make sure to update the path string to point to your exact file location
    with open("SyS/binary/Info.redirect", "r") as file:
        for line in file:
            # Strip spaces/newlines and split values at the equals marker
            cleaned_line = line.strip()
            if "==" in cleaned_line:
                key, value = cleaned_line.split("==", 1)
                key = key.strip()
                value = value.strip()
                
                # Assigns your file parameters directly to validation strings
                if key == "User":
                    target_user = value
                elif key == "Pass":
                    target_pass = value
                    
    return target_user, target_pass

# --- 2. AUTHENTICATION ACTION ---
def check_login():
    # 1. Grab what the user currently typed into the GUI boxes
    entered_username = username_input.get()
    entered_password = password_input.get()
    
    # 2. Dynamically pull the correct answers out of the configuration file
    correct_user, correct_pass = verify_credentials_from_disk()
    
    # 3. Perform the system matching loop validation
    if entered_username == correct_user and entered_password == correct_pass:
        status_label.config(text="Access Granted! Booting VibeOS...", fg="green")
        # [Insert transition to main window here]
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
