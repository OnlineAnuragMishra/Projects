#!/usr/bin/env python
# coding: utf-8

# In[14]:


import cv2
import tkinter as tk
from PIL import Image, ImageTk

class AndroidCameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Xcessor Camera")
        self.root.geometry("600x650")  # Increased height to accommodate button
        self.root.configure(bg="black")
        
        self.video_label = tk.Label(root, bg="black")
        self.video_label.place(x=0, y=0, width=600, height=600)  # Set camera feed dimension
        
        self.capture_button = tk.Button(root, text="Capture Photo", command=self.capture_photo, bg="red", fg="white")
        self.capture_button.place(x=250, y=610, width=100, height=30)  # Positioned below camera feed

        self.capture_in_progress = False
        self.camera = cv2.VideoCapture(0)
        self.update_video_feed()

    def update_video_feed(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = self.resize_image(frame, 600, 600)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(frame)
            self.video_label.config(image=frame)
            self.video_label.image = frame
            self.video_label.after(10, self.update_video_feed)

    def capture_photo(self):
        if not self.capture_in_progress:
            self.capture_in_progress = True
            self.capture_photo_now()

    def capture_photo_now(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite("captured_photo.jpg", frame)
            self.show_image("captured_photo.jpg", "Captured Photo")
            self.capture_in_progress = False

    def show_image(self, file_path, title):
        image = Image.open(file_path)
        image.show(title=title)

    def resize_image(self, image, width, height):
        aspect_ratio = width / height
        img_height, img_width, _ = image.shape
        target_width = int(img_height * aspect_ratio)
        target_size = (target_width, img_height)
        resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
        return resized_image

    def __del__(self):
        if hasattr(self, "camera") and self.camera.isOpened():
            self.camera.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = AndroidCameraApp(root)
    root.mainloop()


# In[ ]:




