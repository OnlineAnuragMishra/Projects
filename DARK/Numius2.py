import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import math
import random

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DARK Numius")
        self.root.geometry("1100x664")  # Adjusted width
        self.root.minsize(900, 664)  # Set minimum width
        self.root.maxsize(1300, 664)  # Set maximum width

        # Remove the logo from the title bar
        self.root.iconbitmap("")

        # Create a gradient background
        bg_image_path = "C:/Project DARK/Img/bg/numius_bg.png"
        self.bg_image = Image.open(bg_image_path)  # Path to your background image
        self.bg_image = self.bg_image.resize((1100, 664), Image.BILINEAR)  # Adjusted size
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#0d47a1')  # Darker blue background
        style.configure('TButton', background='#0d47a1', foreground='white')

        self.create_buttons()

        self.entry = tk.Entry(root, width=52, borderwidth=5, font=("Helvetica", 20), bg="#0d47a1", fg="white")  # Changed display background color
        self.entry.grid(row=1, column=0, columnspan=8, padx=10, pady=10)  # Adjusted columnspan
        self.entry.focus_set()

        xcessor_label = tk.Label(root, text="Numius", font=("Helvetica", 30, "bold"), bg="#0d47a1", fg="white")
        xcessor_label.place(relx=0.5, rely=0.95, anchor="center")

        # Variable to store calculation history
        self.history = []

        # Variable to store last answer
        self.last_answer = None

        # Variable to store memory value
        self.memory = 0

    def create_buttons(self):
        button_texts = [
            ('7', 2, 0, 1, 1), ('8', 2, 1, 1, 1), ('9', 2, 2, 1, 1), ('/', 2, 3, 1, 1), ('C', 2, 4, 1, 1), ('AC', 2, 5, 1, 1), ('Ans', 2, 6, 1, 1), ('MR', 2, 7, 1, 1),
            ('4', 3, 0, 1, 1), ('5', 3, 1, 1, 1), ('6', 3, 2, 1, 1), ('*', 3, 3, 1, 1), ('(', 3, 4, 1, 1), (')', 3, 5, 1, 1), ('M+', 3, 6, 1, 1), ('MC', 3, 7, 1, 1),
            ('1', 4, 0, 1, 1), ('2', 4, 1, 1, 1), ('3', 4, 2, 1, 1), ('-', 4, 3, 1, 1), ('sqrt', 4, 4, 1, 1), ('exp', 4, 5, 1, 1), ('pi', 4, 6, 1, 1), ('%', 4, 7, 1, 1),
            ('0', 5, 0, 1, 1), ('.', 5, 1, 1, 1), ('+', 5, 3, 1, 1), ('sin', 5, 4, 1, 1), ('cos', 5, 5, 1, 1), ('tan', 5, 6, 1, 1), ('log', 5, 7, 1, 1),
            ('^', 6, 0, 1, 1), ('abs', 6, 1, 1, 1), ('Rand', 6, 2, 1, 1), ('History', 6, 3, 1, 5), ('=', 7, 7, 1, 1)  # "=" button placed beneath "log"
        ]

        for text, row, col, rowspan, columnspan in button_texts:
            button = tk.Button(self.root, text=text, width=10, height=2, font=("Helvetica", 15), bg="#0d47a1", fg="white", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, rowspan=rowspan, columnspan=columnspan)

    def on_button_click(self, value):
        if value == 'C':
            current_text = self.entry.get()[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text)
        elif value == 'AC':
            self.entry.delete(0, tk.END)
        elif value == 'Ans':
            self.entry.insert(tk.END, str(self.last_answer))
        elif value == 'MR':
            self.entry.insert(tk.END, str(self.memory))
        elif value == 'M+':
            try:
                self.memory += float(self.entry.get())
            except ValueError:
                pass
        elif value == 'MC':
            self.memory = 0
        elif value == '=':
            try:
                expr = self.entry.get().replace("sqrt", "math.sqrt").replace("exp", "math.exp").replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan").replace("log", "math.log10").replace("pi", "math.pi").replace("^", "**").replace("%", "/100").replace("abs", "abs")
                result = eval(expr)
                self.last_answer = result
                self.history.append(expr + " = " + str(result))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif value == 'History':
            # Open a new window to display history
            history_window = tk.Toplevel(self.root)
            history_window.title("Calculation History")
            history_text = tk.Text(history_window, height=20, width=50)
            history_text.pack()
            for item in self.history:
                history_text.insert(tk.END, item + "\n")
            history_text.config(state=tk.DISABLED)  # Make the text read-only
        elif value == 'Rand':
            self.entry.insert(tk.END, str(random.random()))
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text + value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
