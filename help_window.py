import tkinter as tk


help_window = None

def open_help_window():
    global help_window
    
    if help_window is not None:
        if help_window.winfo_exists():
            help_window.lift()
            return
    
    help_window = tk.Toplevel()
    help_window.title("Key controls")
    help_window.geometry("480x520")
    help_window.iconbitmap("icons/keyboard_icon.ico")
    help_window.resizable(False, False)
    
    control_text = """\n
    - Step forward:   ↑  or  W
    
    - Step back:   ↓  or  S
    
    - Turn left:   ←  or  A
    
    - Turn right:   →  or  D
    
    - Pen up/down:   E
    
    - Show/hide turtle:   F
    
    - Clear the canvas:   Delete
    
    - Screenshot of the canvas:   Print
    """
    
    text_box = tk.Text(help_window, font=("Arial", 10), wrap="word",
                       bg="#f0f0f0", fg="black", bd=0, highlightthickness=0, height=20, width=100)
    text_box.pack(padx=22, pady=20)
    text_box.tag_configure("bold", font=("Arial", 12, "bold"))
    text_box.insert("1.0", "Key controls:", "bold")
    text_box.insert("end", control_text)
    text_box.config(state="disabled")