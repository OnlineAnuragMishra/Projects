import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files(source_folder):
    file_types = {
        'Audio': ['.mp3', '.wav', '.flac'],
        'Video': ['.mp4', '.mkv', '.avi'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Spreadsheets': ['.xlsx', '.csv'],
        'Presentations': ['.pptx'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Code': ['.py', '.java', '.cpp', '.h', '.c', '.html', '.css', '.js'],
        'Executable': ['.exe', '.dll'],
        'Fonts': ['.ttf', '.otf'],
        'Backup': ['.bak'],
        'Databases': ['.db', '.sqlite', '.sql'],
        'Torrents': ['.torrent'],
        'Ebooks': ['.epub', '.mobi'],
        'Fonts': ['.ttf', '.otf'],
        'Logs': ['.log'],
        'Scripts': ['.sh', '.bash'],
        'Documents': ['.doc', '.docx'],
        'PDFs': ['.pdf'],
        'Compressed': ['.zip', '.rar'],
        'Text Files': ['.txt'],
        'Web Files': ['.html', '.css', '.js'],
        'XML Files': ['.xml'],
        'JSON Files': ['.json'],
        'Data Files': ['.csv', '.dat'],
        'Spreadsheets': ['.xlsx', '.xls'],
        'Presentations': ['.pptx', '.ppt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav', '.ogg'],
        'Code': ['.py', '.java', '.cpp'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Fonts': ['.ttf', '.otf'],
        'Web Development': ['.html', '.css', '.js'],
        'Documents': ['.doc', '.docx', '.pdf'],
        'Excel Files': ['.xlsx', '.xls'],
        'PowerPoint Files': ['.pptx', '.ppt'],
        'Text Files': ['.txt'],
        'Config Files': ['.ini', '.cfg'],
        'Scripts': ['.sh', '.bat'],
        'Batch Files': ['.bat', '.cmd'],
        'Shell Scripts': ['.sh'],
        'Database Files': ['.db', '.sql'],
        'Torrents': ['.torrent'],
        'Ebooks': ['.pdf', '.epub', '.mobi'],
        'Installers': ['.exe', '.msi'],
        'Logs': ['.log'],
        'Temp Files': ['.tmp'],
        'Images': ['.jpg', '.jpeg', '.png'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Audio': ['.mp3', '.wav'],
        'Compressed Files': ['.zip', '.rar', '.tar', '.gz'],
        'Virtual Machines': ['.vdi', '.vmwarevm', '.vbox'],
        'CAD Files': ['.dwg', '.dxf'],
        'Gaming': ['.exe', '.iso'],
        'Spreadsheets': ['.xlsx', '.csv'],
        'Vector Graphics': ['.svg', '.ai'],
        '3D Models': ['.obj', '.stl'],
        'Source Code': ['.py', '.cpp', '.java'],
        
    }

    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            file_extension = os.path.splitext(filename)[1].lower()

            destination_folder = None
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(source_folder, category)
                    break

            if destination_folder:
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.move(
                    os.path.join(source_folder, filename),
                    os.path.join(destination_folder, filename)
                )

    return "Files organized successfully!"

def organize_button_clicked():
    source_folder = filedialog.askdirectory(
        title='Select a folder to organize',
        mustexist=True
    )

    if source_folder:
        result_label.config(text="Organizing...")
        result_message = organize_files(source_folder)
        result_label.config(text=result_message)

root = tk.Tk()
root.title("ZenSpace 2")
root.geometry("996x664")
root.configure(bg="black")

bg_image = tk.PhotoImage(file="C:/Users/anura/OneDrive/Desktop/Project DARK/Img/bg/ui_hs_bg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(root, text="ZenSpace 2", font=("Helvetica", 24), fg="white", bg="grey")
title_label.pack(pady=10)

tagline_label = tk.Label(root, text="Arrange your impossible File clutters", font=("Helvetica", 12), fg="white", bg="grey")
tagline_label.pack()

organize_button = tk.Button(root, text="Organize Files", command=organize_button_clicked, font=("Helvetica", 18))
organize_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="white", bg="grey")
result_label.pack(pady=20)

# Add build number label
build_number = "2.0.1.4D2 (Beta Build)"
build_label = tk.Label(root, text=build_number, font=("Helvetica", 10), fg="white", bg="grey")
build_label.place(relx=1, rely=1, anchor='se')

root.mainloop()
