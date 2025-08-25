"""
-----------------------------------
Project: Password Generator (GUI)
Author : Your Name
Date   : 23-Aug-2025
Description:
    A beginner-friendly GUI PasswordGenerator
    built with Tkinter in Python..
-----------------------------------
"""
import random
import string
import tkinter as tk
from tkinter import messagebox

def password_generator(number):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=number))

def gui():
    def on_click():
        try:
            number = int(entry.get())
            if number <= 0:
                output_label.config(text="❌ Enter a positive number!")
                return
            password = password_generator(number)
            output_label.config(text=password)
        except ValueError:
            output_label.config(text="❌ Please enter a valid number!")

    def copy_to_clipboard():
        password = output_label.cget("text")
        if password and "❌" not in password:
            window.clipboard_clear()
            window.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

    # Main window
    window = tk.Tk()
    window.title("🔑 Password Generator")
    window.geometry("400x300")
    window.configure(bg="#f0f0f0")

    # Title label
    title = tk.Label(window, text="Random Password Generator", 
                     font=("Arial", 16, "bold"), fg="white", bg="#333")
    title.pack(fill="x", pady=10)

    # Input section
    frame = tk.Frame(window, bg="#f0f0f0")
    frame.pack(pady=10)

    entrylabel = tk.Label(frame, text="Enter Password Length:", 
                          font=("Arial", 12), bg="#f0f0f0")
    entrylabel.grid(row=0, column=0, padx=5, pady=5)

    entry = tk.Entry(frame, font=("Arial", 12), width=10, justify="center")
    entry.grid(row=0, column=1, padx=5, pady=5)

    # Buttons
    button = tk.Button(window, text="Generate Password", 
                       font=("Arial", 12), bg="#4CAF50", fg="white", 
                       relief="flat", command=on_click)
    button.pack(pady=10)

    copy_button = tk.Button(window, text="Copy to Clipboard", 
                            font=("Arial", 12), bg="#2196F3", fg="white", 
                            relief="flat", command=copy_to_clipboard)
    copy_button.pack(pady=5)

    # Output section
    output_label = tk.Label(window, text="", font=("Consolas", 14), 
                            fg="blue", bg="white", width=30, height=2, 
                            relief="solid", bd=1)
    output_label.pack(pady=10)

    window.mainloop()

gui()

