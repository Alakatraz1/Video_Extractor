import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def convert_video_to_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Command to extract frames
    command = f"ffmpeg -i {video_path} -q:v 1 {output_folder}/frame_%d.jpg"

    # Execute the command
    subprocess.call(command, shell=True)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_folder)

def convert_video():
    video_path = entry.get()
    output_folder = output_entry.get()
    if not os.path.exists(video_path):
        tk.messagebox.showerror("Error", "Please select a valid video file.")
        return
    if not output_folder:
        tk.messagebox.showerror("Error", "Please specify the output folder.")
        return

    convert_video_to_frames(video_path, output_folder)
    tk.messagebox.showinfo("Success", "Video converted to frames successfully!")

# Create the main window
root = tk.Tk()
root.title("Video to Frames Converter")

# Create widgets
tk.Label(root, text="Select Video File:").grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=5, pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_video)
convert_button.grid(row=2, column=1, padx=5, pady=5)

# Start the main event loop
root.mainloop()
