import tkinter as tk


project_information_window = None

def open_project_information_window():
    global project_information_window
    
    if project_information_window is not None:
        if project_information_window.winfo_exists():
            project_information_window.lift()
            return
    
    project_information_window = tk.Toplevel()
    project_information_window.title("Project information")
    project_information_window.geometry("660x350")
    project_information_window.iconbitmap("icons/project_icon.ico")
    project_information_window.resizable(False, False)
    
    information_text = """\n
    - Risovalka is a small project that was made as a portfolio.
    
    - Python programming language was used for its creation.
    
    - The author of this project is Aleksander Ontin.
    
    - It was created in February 2025, starting on the 12th and ending on the 18th.
    """
    
    text_box = tk.Text(project_information_window, font=("Arial", 10), wrap="word",
                       bg="#f0f0f0", fg="black", bd=0, highlightthickness=0, height=20, width=110,
                       spacing2=10)
    text_box.pack(padx=22, pady=20)
    text_box.tag_configure("bold", font=("Arial", 12, "bold"))
    text_box.insert("1.0", "Project information:", "bold")
    text_box.insert("end", information_text)
    text_box.config(state="disabled")