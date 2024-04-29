import tkinter as tk
import sqlite3
import subprocess

class AccountCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark Account Creator")
        self.root.geometry("500x600")
        self.root.configure(bg="black")

        # Set application icon with absolute path
        self.root.iconbitmap(r'C:/Project DARK/ico/login_ico/icons8-login-64.png')

        self.heading_label = tk.Label(root, text="DARK(c) Account", font=("Helvetica", 24, "bold"), bg="black", fg="white")
        self.heading_label.pack(pady=20)

        self.name_label = tk.Label(root, text="Name:", font=("Helvetica", 12), bg="black", fg="white")
        self.name_label.pack()

        self.name_entry = tk.Entry(root, font=("Helvetica", 12))
        self.name_entry.pack()

        self.username_label = tk.Label(root, text="Username:", font=("Helvetica", 12), bg="black", fg="white")
        self.username_label.pack()

        self.username_entry = tk.Entry(root, font=("Helvetica", 12))
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:", font=("Helvetica", 12), bg="black", fg="white")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
        self.password_entry.pack()

        self.submit_button = tk.Button(root, text="Create DARK Account", font=("Helvetica", 14), command=self.create_account)
        self.submit_button.pack(pady=20)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 12), bg="black", fg="green")
        self.status_label.pack()

    def create_account(self):
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if name and username and password:
            self.store_user_in_database(name, username, password)
            self.status_label.config(text="Account created successfully!")
            self.root.after(3000, self.close_window)

    def store_user_in_database(self, name, username, password):
        conn = sqlite3.connect("acc_db.db")
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           username TEXT NOT NULL UNIQUE,
                           password TEXT NOT NULL)''')

        try:
            cursor.execute("INSERT INTO accounts (name, username, password) VALUES (?, ?, ?)", (name, username, password))
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            self.status_label.config(text="Username already exists.")

    def close_window(self):
        self.root.destroy()
        subprocess.run([r"C:\Project DARK\Modules\dist\login_acc\login_acc.exe"])

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountCreator(root)
    root.mainloop()
