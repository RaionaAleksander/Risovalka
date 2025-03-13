import os
from PIL import ImageGrab

def create_screenshot_folder(folder_name="screenshots"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def generate_filename(folder_name="screenshots"):
    index = 1
    while os.path.exists(os.path.join(folder_name, f"screenshot_{index}.png")):
        index += 1
    return os.path.join(folder_name, f"screenshot_{index}.png")


def save_canvas_screenshot(root, canvas, turtle_obj):
    folder = create_screenshot_folder()
    filename = generate_filename(folder)
    
    was_visible = turtle_obj.isvisible()
    
    if was_visible:
        turtle_obj.hideturtle()
    
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    image = ImageGrab.grab((x, y, x1, y1))
    image.save(filename)

    print(f"Screenshot saved: {filename}")
    
    if was_visible:
        turtle_obj.showturtle()