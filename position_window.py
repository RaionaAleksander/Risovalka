import tkinter as tk

def open_position_window(parent, set_position_callback, current_x, current_y, current_angle):
    position_window = tk.Toplevel(parent)
    position_window.geometry("420x260")
    position_window.title("Position")
    position_window.iconbitmap("icons/position_icon.ico")
    position_window.resizable(False, False)

    frame = tk.Frame(position_window)
    frame.pack(pady=20, padx=20)

    tk.Label(frame, text="X (-500 - 500):", font=("Arial", 10), width=15, anchor="w").grid(row=0, column=0, sticky="w", pady=5)
    entry_x = tk.Entry(frame, font=("Arial", 10), width=6)
    entry_x.insert(0, str(int(current_x)))
    entry_x.grid(row=0, column=1, padx=5)

    tk.Label(frame, text="Y (-500 - 500):", font=("Arial", 10), width=15, anchor="w").grid(row=1, column=0, sticky="w", pady=5)
    entry_y = tk.Entry(frame, font=("Arial", 10), width=6)
    entry_y.insert(0, str(int(current_y)))
    entry_y.grid(row=1, column=1, padx=5)

    tk.Label(frame, text="Angle (0 - 359):", font=("Arial", 10), width=15, anchor="w").grid(row=2, column=0, sticky="w", pady=5)
    entry_angle = tk.Entry(frame, font=("Arial", 10), width=6)
    entry_angle.insert(0, str(int(current_angle)))
    entry_angle.grid(row=2, column=1, padx=5)

    def apply_changes():
        x = int(entry_x.get())
        y = int(entry_y.get())
        angle = int(entry_angle.get())

        set_position_callback(x, y, angle)
        position_window.destroy()

    btn_apply = tk.Button(position_window, text="Apply", width=10, command=apply_changes)
    btn_apply.pack(pady=10)

    position_window.mainloop()