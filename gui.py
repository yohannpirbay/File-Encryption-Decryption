import tkinter as tk
from tkinter import messagebox
from encryption import *
from pyperclip import copy
from tkinter import filedialog
from cryptography.fernet import InvalidToken

# Class that handles the GUI for the application
class MyGUI:

    # Creates the window
    def __init__(self):
        self.file = ""
        self.root = tk.Tk()
        self.root.title("File Encryption")
        self.root.geometry("500x200")
        self.root.resizable(False, False)

        self.file_frame = tk.Frame(self.root)
        self.file_frame.pack(pady=(25, 0))

        self.select_button = tk.Button(self.file_frame, text="Select File", command=self.select_file)
        self.select_button.grid(row=0, column=0)

        self.file_label = tk.Label(self.file_frame, )
        self.file_label.grid(row=0, column=1)

        self.generate_button = tk.Button(self.root, text="Generate key", command=self.on_generate)
        self.generate_button.pack(pady=(10, 0))

        self.key_frame = tk.Frame(self.root)
        self.key_frame.pack(pady=(10, 0))

        self.key_label = tk.Label(self.key_frame, text="Input key here: ")
        self.key_label.grid(row=0, column=0)

        self.key_display = tk.Entry(self.key_frame, show='*')
        self.key_display.grid(row=0, column=1)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=(10, 0))

        self.encrypt_button = tk.Button(self.button_frame, text="Encrypt", command=self.on_encrypt)
        self.encrypt_button.grid(row=0, column=0)

        self.decrypt_button = tk.Button(self.button_frame, text="Decrypt", command=self.on_decrypt)
        self.decrypt_button.grid(row=0, column=1)

        self.root.mainloop()
    
    # Generates a key, copies it to the clipboard and displays it hidden for the user
    def on_generate(self):
        key = generate_key()
        copy(key)
        self.key_display.insert(0, key)

    # Truncates the file path to fit the window
    def truncate_file_path(self, file_path):
        if len(file_path) > 40:
            return  file_path[0:10] + "..." + file_path[-(40 - 3):]
        return file_path
    
    # Checks if the key is valid
    def validate_key(self):
        try:
            fernet = Fernet(self.key_display.get())
            return True
        except (ValueError, TypeError, InvalidToken):
            return False
    
    # Opens a dialogue box for file selection
    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a file", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        elif file_path.endswith('.txt'):
            self.file = file_path
            truncated_path = self.truncate_file_path(file_path)
            self.file_label.config(text=truncated_path)
        else:
            messagebox.showerror("Invalid", "Invalid selection, please select a .txt file!")

    # Encrypts a file
    def on_encrypt(self):
        if self.file == "":
            messagebox.showerror("Invalid", "Please select a file!")
        elif self.key_display.get() == "":
            messagebox.showerror("Invalid", "Please enter an encryption key!")
        elif not self.validate_key():
            messagebox.showerror("Invalid", "The key is not valid!")
        else:
            encrypt_file(self.file, self.key_display.get())

    # Decrypts a file
    def on_decrypt(self):
        if self.file == "":
            messagebox.showerror("Invalid", "Please select a file!")
        elif self.key_display.get() == "":
            messagebox.showerror("Invalid", "Please enter an encryption key!")
        elif not self.validate_key():
            messagebox.showerror("Invalid", "The key is not valid!")
        else:
            try:
                decrypt_file(self.file, self.key_display.get())
            except InvalidToken as error:
                messagebox.showerror("Decryption Error", str(error))

# Starts the application
def run():
    MyGUI()