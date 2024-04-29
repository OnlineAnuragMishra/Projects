import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to DARK")

        # Load the background image and keep a reference
        self.bg_image = Image.open(r"C:\Project DARK\Img\bg\ui_wel_wel.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Get the size of the background image
        width, height = self.bg_image.size

        # Resize the window to match the size of the background image
        self.root.geometry(f"{width}x{height}")

        # Create a label for the background image and place it in the window
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0)

        # Raise the logo label to the top of the stacking order
        self.bg_label.lift()

        xcessor_label = tk.Label(root, text="DARK ©", font=("Pulpen Snowman", 24, "bold"), bg="white", fg="black")
        xcessor_label.pack()

        text = """Welcome to DARK© – the Dynamic Application Resource Kit"""
        description_label = tk.Label(root, text=text, font=("Helvetica", 12), bg="white", wraplength=800, justify="center")
        description_label.pack(pady=20)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 14))

        self.google_login_button = ttk.Button(root, text="Login with Google", command=self.show_google_unavailable)
        self.google_login_button.pack(side="bottom", pady=10)

        self.signup_button = ttk.Button(root, text="Sign Up with DARK©", command=self.sign_up_with_dark)
        self.signup_button.pack(side="bottom", pady=10)

        self.signin_button = ttk.Button(root, text="SignIn with DARK©", command=self.run_login_acc)
        self.signin_button.pack(side="bottom", pady=10)
        
        self.skip_button = ttk.Button(root, text="Skip sign in as Guest", command=self.run_homescreen)
        self.skip_button.pack(side="bottom", pady=10)

    def run_login_acc(self):
        try:
            subprocess.run([r"C:\Project DARK\Modules\dist\login_acc\login_acc.exe"])
        except Exception as e:
            print("Error:", e)

    def sign_up_with_dark(self):
        try:
            subprocess.run([r"C:\Project DARK\Modules\dist\cr_us_Acc\cr_us_Acc.exe"])
        except Exception as e:
            print("Error:", e)

    def show_google_unavailable(self):
        google_unavailable_window = tk.Toplevel()
        google_unavailable_window.title("Service Temporarily Unavailable")
        google_unavailable_window.geometry("400x200")
        google_unavailable_window.configure(bg="black")

        message_label = tk.Label(google_unavailable_window, text="Service Temporarily Unavailable", font=("Helvetica", 16), bg="black", fg="white")
        message_label.pack(pady=50)

        # Close the window after 3000 milliseconds (3 seconds)
        google_unavailable_window.after(3000, google_unavailable_window.destroy)

    def run_homescreen(self):
        try:
            subprocess.run([r"C:\Project DARK\Modules\dist\homescreen\homescreen.exe"])
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeScreen(root)
    root.mainloop()
