#!/usr/bin/env python
# coding: utf-8

# In[20]:


import tkinter as tk
import sqlite3
import subprocess
import webbrowser

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("300x500")
        self.root.configure(bg="black")  # Set the background color to black

        # Set application icon
        self.root.iconbitmap(r'C:\Users\anura\Desktop\Project Xcessor\ico\login_ico\icons8-login-64.png')

        self.heading_label = tk.Label(root, text="DARK(c) Login Page", font=("Helvetica", 16, "bold"), bg="black", fg="white")
        self.heading_label.pack(pady=20)

        self.username_label = tk.Label(root, text="Username:", font=("Helvetica", 12), bg="black", fg="white")
        self.username_label.pack()

        self.username_entry = tk.Entry(root, font=("Helvetica", 12))
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:", font=("Helvetica", 12), bg="black", fg="white")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", font=("Helvetica", 14), command=self.login)
        self.login_button.pack(pady=20)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 12), bg="black", fg="green")
        self.status_label.pack()

    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username and entered_password:
            if self.check_credentials(entered_username, entered_password):
                self.status_label.config(text="Login Successful")
                self.root.after(3000, self.run_another_program)
            else:
                self.status_label.config(text="Login Failed")
                
        if entered_username and entered_password:
            if self.check_credentials(entered_username, entered_password):
                self.status_label.config(text="Login Successful")
                self.root.after(4000, self.close_window)  # Close window after 4 seconds
            else:
                self.status_label.config(text="Login Failed")

    def check_credentials(self, entered_username, entered_password):
        conn = sqlite3.connect("acc_db.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM accounts WHERE username = ?", (entered_username,))
        user = cursor.fetchone()

        conn.close()

        if user and user[3] == entered_password:
            return True
        else:
            return False

    def run_another_program(self):
        subprocess.run(["python", "C:/Users/anura/Desktop/Project Xcessor/modules/Home_sc_default.py"])  # Replace with the correct path

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


# In[ ]:




