import os
import tkinter as tk
from tkinter import *
from tkinter import Tk, filedialog, messagebox, ttk
from pytube import YouTube

class YoutubeDownloader:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YouTube Downloader")
        self.root.geometry("800x400")
        self.root.config(bg="#F0F0F0")
        self.root.resizable(False, False)

        # Header label
        header_label = tk.Label(self.root, text="Download YouTube Videos", font=("Arial", 24, "bold"), fg="#D32F2F", bg="#F0F0F0")
        header_label.pack(pady=20)

        # URL entry
        url_frame = tk.Frame(self.root, bg="#F0F0F0")
        url_frame.pack()
        url_label = tk.Label(url_frame, text="Enter YouTube URL:", font=("Arial", 14, "bold"), fg="#212121", bg="#F0F0F0")
        url_label.pack(side=tk.LEFT, padx=5, pady=10)
        self.url_entry = tk.Entry(url_frame, width=50, font=("Arial", 14), bg="#FFFFFF", relief=tk.SOLID, bd=1)
        self.url_entry.pack(side=tk.LEFT, padx=5, pady=10)

        # Directory selector
        dir_frame = tk.Frame(self.root, bg="#F0F0F0")
        dir_frame.pack(pady=10)
        dir_label = tk.Label(dir_frame, text="Save video to:", font=("Arial", 14, "bold"), fg="#212121", bg="#F0F0F0")
        dir_label.pack(side=tk.LEFT, padx=5, pady=10)
        self.dir_entry = tk.Entry(dir_frame, width=40, font=("Arial", 14), bg="#FFFFFF", relief=tk.SOLID, bd=1)
        self.dir_entry.pack(side=tk.LEFT, padx=5, pady=10)
        self.dir_button = tk.Button(dir_frame, text="Browse", font=("Arial", 14), bg="#D32F2F", fg="#FFFFFF", activebackground="#C62828", activeforeground="#FFFFFF", relief=tk.FLAT, command=self.select_directory)
        self.dir_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Download button
        self.download_button = tk.Button(self.root, text="Download", font=("Arial", 16, "bold"), bg="#D32F2F", fg="#FFFFFF", activebackground="#C62828", activeforeground="#FFFFFF", relief=tk.FLAT, command=self.download)
        self.download_button.pack(pady=30)

        self.root.mainloop()

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        self.dir_entry.delete(0, tk.END)
        self.dir_entry.insert(0, self.directory)

    def download(self):
        url = self.url_entry.get()
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_size = stream.filesize
        filename = stream.default_filename
        filepath = f"{self.directory}/{filename}"
        stream.download(self.directory, filename=stream.default_filename, 
                            on_progress_callback=lambda stream, chunk, bytes_remaining: 
                            self.update_progress_bar(filepath, stream.filesize - bytes_remaining))

        stream.download(output_path=self.directory, filename=filename)
        messagebox.showinfo(title="Success", message="Download complete!")


    # Open the downloaded file using the default program
        os.startfile(filepath)



if __name__ == "__main__":
    downloader = YoutubeDownloader()

