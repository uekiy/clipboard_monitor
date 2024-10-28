import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageGrab, Image, ImageTk
import os
import time
from datetime import datetime

class ClipboardMonitor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clipboard Monitor")
        self.geometry("400x300")
        self.resizable(True, True)
        
        self.save_dir = ""
        self.monitoring = False
        self.prev_clipboard = None
        
        self.create_widgets()
    
    def create_widgets(self):
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background="white")
        self.style.configure("Custom.TButton", padding=6, font=("Helvetica", 10))
        
        self.frame = ttk.Frame(self, padding=10, style="Custom.TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.clipboard_icon = self.load_icon("clipboard.png")
        self.icon_label = ttk.Label(self.frame, image=self.clipboard_icon)
        self.icon_label.pack()
        
        self.status_label = ttk.Label(self.frame, text="Monitoring: OFF", font=("Helvetica", 12))
        self.status_label.pack()
        
        self.toggle_button = ttk.Button(self.frame, text="Start Monitoring", command=self.toggle_monitoring, style="Custom.TButton")
        self.toggle_button.pack(pady=10)
        
        self.select_button = ttk.Button(self.frame, text="Select Save Directory", command=self.select_directory, style="Custom.TButton")
        self.select_button.pack()
        
        self.dir_label = ttk.Label(self.frame, text="Save Directory: Not Selected", wraplength=350)
        self.dir_label.pack()
        
        self.save_status_label = ttk.Label(self.frame, text="", foreground="green")
        self.save_status_label.pack()
        
        self.after(1000, self.check_clipboard)
        
    def load_icon(self, filename):
        icon_path = os.path.join(os.path.dirname(__file__), filename)
        icon = Image.open(icon_path)
        icon = icon.resize((64, 64), Image.Resampling.LANCZOS)
        icon = ImageTk.PhotoImage(icon)
        return icon
        
    def toggle_monitoring(self):
        if not self.monitoring:
            if not self.save_dir:
                self.select_directory()
            if self.save_dir:
                self.monitoring = True
                self.status_label.config(text="Monitoring: ON")
                self.toggle_button.config(text="Stop Monitoring")
        else:
            self.monitoring = False
            self.status_label.config(text="Monitoring: OFF")
            self.toggle_button.config(text="Start Monitoring")
    
    def select_directory(self):
        self.save_dir = filedialog.askdirectory(title="Select Save Directory")
        if self.save_dir:
            self.dir_label.config(text=f"Save Directory: {self.save_dir}")
        else:
            self.dir_label.config(text="Save Directory: Not Selected")
    
    def check_clipboard(self):
        if self.monitoring:
            try:
                img = ImageGrab.grabclipboard()
                if img is not None and img != self.prev_clipboard:
                    self.prev_clipboard = img
                    self.save_image(img)
            except:
                pass
        self.after(1000, self.check_clipboard)
    
    def save_image(self, img):
        width, height = img.size
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{width}x{height}_{timestamp}.png"
        filepath = os.path.join(self.save_dir, filename)
        img.save(filepath)
        print(f"Image saved: {filepath}")
        
        self.save_status_label.config(text=f"✔ {filename} saved.")
        self.after(5000, self.clear_save_status)
    
    def clear_save_status(self):
        self.save_status_label.config(text="")

def main():
    app = ClipboardMonitor()
    app.mainloop()

if __name__ == "__main__":
    main()
