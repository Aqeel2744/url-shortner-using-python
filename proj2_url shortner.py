import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Function to shorten URL
def shorten_url():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL to shorten.")
        return
    
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        result_label.config(text=f"Shortened URL: {short_url}")
        copy_button.config(state=tk.NORMAL)  
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        copy_button.config(state=tk.DISABLED)  

# Function to copy the shortened URL to the clipboard
def copy_to_clipboard():
    short_url = result_label.cget("text").replace("Shortened URL: ", "")
    root.clipboard_clear()
    root.clipboard_append(short_url)
    messagebox.showinfo("Copied!")

# Create the main application window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x250")
root.configure(bg="#F0EAD6") 

# URL Entry Label
url_label = tk.Label(root, text="Enter URL:", bg="#F0EAD6") 
url_label.pack(pady=10)

# URL Entry
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Shorten Button
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url, bg='purple', fg='white')
shorten_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", wraplength=350, bg="#F0EAD6")  # Matching background
result_label.pack(pady=10)

# Copy Button
copy_button = tk.Button(root, text="Copy URL", command=copy_to_clipboard, state=tk.DISABLED, bg='purple', fg='white')
copy_button.pack(pady=10)
root.mainloop()



