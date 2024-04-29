import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess
import sys

class ButtonDemo:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("996x664")

        # Define the absolute path to the background image
        bg_image_path = "C:/Project DARK/Img/bg/ui_hs_bg.png"

        bg_image = Image.open(bg_image_path)  # Load the background image using the absolute path
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_label = tk.Label(root, text="DARK SOFTWARE SUITE", font=("Pulpen Snowman", 24, "bold"), fg="black")
        title_label.place(x=20, y=20)

        user_label = tk.Label(root, text=f"Welcome, Dear {username}", font=("Helvetica", 14), bg="black", fg="white")
        user_label.place(x=20, y=90)

        button_data = [
            ("Parasnap", "XPhoto.py"),
            ("Numius", "Numius2.py"),
            ("ZenSpace", "DeClutter.py"),
            ("Lensnap", "XCam.py"),
            ("SkyNav", "xBrowser.py"),  
            ("Install Modules", "install_modules")
        ]

        for row, (text, script) in enumerate(button_data, start=3):
            command = lambda s=script: self.run_script(s)
            button = tk.Button(root, text=text, command=command, fg="black", font=("Helvetica", 12))
            button.place(x=130, y=150+(row-3)*50)

        # Add build number label
        build_number = "2.0.1.4D2 (Beta Build)"
        build_label = tk.Label(root, text=build_number, font=("Helvetica", 10), fg="black")
        build_label.place(relx=1, rely=1, anchor='se')

    def run_script(self, script_name):
        if script_name == "install_modules":
            self.install_modules()
        else:
            script_path = os.path.join("C:/Project DARK/Modules", script_name)  # Adjust according to your folder structure
            subprocess.Popen(["python", script_path])

    def install_modules(self):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python", "Pillow", "pyqt5", "PyQtWebEngine"])
            messagebox.showinfo("Module Installation", "Modules installed successfully!")
        except subprocess.CalledProcessError:
            messagebox.showerror("Module Installation", "Failed to install modules.")

if __name__ == "__main__":
    root = tk.Tk()
    username = sys.argv[1] if len(sys.argv) > 1 else "User"  # Get username from command-line argument
    app = ButtonDemo(root, username)
    root.mainloop()
