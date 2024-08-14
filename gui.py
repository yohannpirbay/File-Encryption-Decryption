import tkinter as tk
from tkinter import messagebox
from encryption import *
from pyperclip import copy

# Class that handles the GUI for the application
class MyGUI:

    # Creates the window
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Encryption")
        self.root.geometry("400x150")
        self.root.resizable(False, False)

        self.key_frame = tk.Frame(self.root)
        self.key_frame.pack(pady=(30, 0))

        self.key_label = tk.Label(self.key_frame, text="Input key here: ")
        self.key_label.grid(row=0, column=0)

        self.key_display = tk.Entry(self.key_frame, show='*')
        self.key_display.grid(row=0, column=1)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.encrypt_button = tk.Button(self.button_frame, text="Encrypt")
        self.encrypt_button.grid(row=0, column=0)

        self.decrypt_button = tk.Button(self.button_frame, text="Decrypt")
        self.decrypt_button.grid(row=0, column=1)

        self.generate_button = tk.Button(self.root, text="Generate a key", command=self.on_generate)
        self.generate_button.pack()

        self.root.mainloop()
    
    def on_generate(self):
        copy(generate_key())

MyGUI()