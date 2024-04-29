import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class PhotoViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ParaSnap")
        self.root.geometry("996x664")

        self.load_ui_elements()
        self.configure_ui()

        self.image_paths = []
        self.current_image_index = 0

    def load_ui_elements(self):
        # Load the placeholder image
        self.placeholder_path = "C:/Users/anura/OneDrive/Desktop/Project DARK/Img/bg/Placeholder-_-Begrippenlijst-800x450.webp"
        self.default_placeholder_photo = ImageTk.PhotoImage(Image.open(self.placeholder_path))

    def configure_ui(self):
        self.configure_bg_label()
        self.configure_title()
        self.configure_image_label()
        self.configure_buttons()

    def configure_bg_label(self):
        # Load the background image
        bg_path = "C:/Users/anura/OneDrive/Desktop/Project DARK/Img/bg/photo.jpg"
        self.bg_photo = ImageTk.PhotoImage(Image.open(bg_path))
        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor=tk.NW)

    def configure_title(self):
        # Use a simple text label as title with font Agency FB
        self.title_label = tk.Label(self.root, text="PARASNAP", font=("Agency FB", 24), bg="violet", fg="white")
        self.title_label.pack(side=tk.TOP, fill=tk.X)

    def configure_buttons(self):
        self.button_frame = tk.Frame(self.root, bg="violet")
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)

        button_texts = ["Scan", "Next", "Previous", "Open Folder", "Quit"]
        button_commands = [self.browse_folder, self.next_photo, self.previous_photo, self.open_folder_containing_image, self.root.quit]

        for text, command in zip(button_texts, button_commands):
            ttk.Button(self.button_frame, text=text, command=command).pack(side=tk.LEFT, padx=5, pady=5)

    def configure_image_label(self):
        self.image_label = tk.Label(self.root, bg="violet")
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.image_label.bind("<Double-Button-1>", self.open_image_default_viewer)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.scan_images_in_folder(folder_path)

    def scan_images_in_folder(self, folder_path):
        self.image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith((".jpg", ".png"))]
        self.current_image_index = 0
        self.update_displayed_image()

    def next_photo(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.update_displayed_image()

    def previous_photo(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.update_displayed_image()

    def open_image_default_viewer(self, event):
        if self.image_paths:
            image_path = self.image_paths[self.current_image_index]
            self.open_with_default_viewer(image_path)

    def open_with_default_viewer(self, image_path):
        os.startfile(image_path)

    def open_folder_containing_image(self):
        if self.image_paths:
            image_path = self.image_paths[self.current_image_index]
            folder_path = os.path.dirname(image_path)
            os.startfile(folder_path)

    def update_displayed_image(self):
        if self.image_paths:
            image_path = self.image_paths[self.current_image_index]
            image = Image.open(image_path)

            max_width = self.image_label.winfo_width()
            max_height = self.image_label.winfo_height()

            if image.width > max_width or image.height > max_height:
                image = image.resize((int(image.width / 5), int(image.height / 5)), Image.LANCZOS)
            else:
                image = image.resize((int(image.width / 5), int(image.height / 5)), Image.LANCZOS)

            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        else:
            self.image_label.configure(image=self.default_placeholder_photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoViewerApp(root)
    app.root.wm_attributes("-topmost", True)
    root.mainloop()
