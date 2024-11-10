import tkinter as tk
from tkinter import simpledialog

def get_user_input(prompt="Enter value:", title="Input"):
    # Create the root window but hide it
    root = tk.Tk()
    root.withdraw()
    
    # Show the input dialog and get value
    user_input = simpledialog.askstring(title, prompt)
    
    # Destroy the root window
    root.destroy()
    
    return user_input