import tkinter as tk
from tkinter import filedialog
import module.write_env as we

def _browse_file_include_env(key_env):
    # Open a file dialog and store the selected file path
    file_path = filedialog.askopenfilename()
    if file_path:  # If a file was selected
        print(f"Selected file: {file_path}")
        we.write_to_env(key_env, file_path)
    else:
        print("Please, select a file")

def browseFileForEnv(keyEnv, textContext):
    root = tk.Tk()
    root.title("Select File")

    text_context = tk.Text(
        root, 
        height=3, 
        width=40, 
        wrap=tk.WORD,
        font=('Arial', 10)
    )
    text_context.insert('1.0', textContext)
    text_context.configure(state='disabled')
    text_context.pack(pady=10, padx=20)
    
    browse_button = tk.Button(root, text="Browse for a file...", command=lambda: _browse_file_include_env(keyEnv))
    browse_button.pack(pady=20)
    
    exit_button = tk.Button(root,text="Done..", command=root.destroy)
    exit_button.pack(pady=20)
    
    root.mainloop()

# ... rest of the existing code ...