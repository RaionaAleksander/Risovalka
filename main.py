# Imports
import tkinter as tk
import turtle
from tkinter import colorchooser

from help_window import open_help_window
from project_information_window import open_project_information_window
from position_window import open_position_window
from screenshot_canvas import save_canvas_screenshot

# Functions
def move_forward(event=None):
    t.forward(t_step)
    update_position()

def move_backward(event=None):
    t.backward(t_step)
    update_position()

def turn_left(event=None):
    t.left(t_turn)
    update_position()

def turn_right(event=None):
    t.right(t_turn)
    update_position()
    
def update_position():
    x, y = int(t.xcor()), int(t.ycor())
    angle = int(t.heading())
    label_turtle_position_values.config(text=f"X: {x}, Y: {y}, Angle: {angle}°")
    
def set_new_position(x, y, angle):
    global t_pen_down
    
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    
    if t_pen_down:
        t.pendown()
    update_position()
    
def change_pen_size(event=None):
    value = pen_option_size_entry.get()
    if value.isdigit():
        t.pensize(int(value))

def change_pen_step(event=None):
    global t_step
    value = pen_option_step_entry.get()
    if value.isdigit(): 
        t_step = int(value)
        
def change_pen_turn(event=None):
    global t_turn
    value = pen_option_turn_entry.get()
    if value.isdigit(): 
        t_turn = int(value)

def change_pen_color(event=None):
    color = colorchooser.askcolor()[1]
    if color:
        t.pencolor(color)
        label_option_pen_color_display.config(fg=color)
        
def change_turtle_color(event=None):
    color = colorchooser.askcolor()[1]
    if color:
        t.fillcolor(color)
        label_option_turtle_color_display.config(fg=color)

def change_turtle_shape(shape):
    lowercase_shape = shape.lower()
    t.shape(lowercase_shape)
    label_option_shape_display.config(text=lowercase_shape)

def toggle_pen(event=None):
    global t_pen_down
    if t_pen_down:
        t.penup()
        btn_pen_updown.config(text="Pen down")
    else:
        t.pendown()
        btn_pen_updown.config(text="Pen up")
    t_pen_down = not t_pen_down

def toggle_turtle(event=None):
    global t_visible
    if t_visible:
        t.hideturtle()
        btn_turtle_visibility.config(text="Show turtle")
    else:
        t.showturtle()
        btn_turtle_visibility.config(text="Hide turtle")
    t_visible = not t_visible
    
def clear_canvas():
    t.clear()

def remove_focus(event):
    if event.widget not in [pen_option_step_entry, pen_option_turn_entry, pen_option_size_entry]:
        root.focus_set()

root = tk.Tk()
root.title("Risovalka")
root.geometry("1920x1080")
root.iconbitmap("icons/drawing_icon.ico")
root.resizable(False, False)

canvas_width = 1000
canvas_height = 1000

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white", highlightthickness=2, highlightbackground="black")
canvas.place(x=40, y=40)

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")

t = turtle.RawTurtle(screen)
t.speed(10)
t.pensize(1)
t_step = 10
t_turn = 10
t_pen_down = True
t_visible = True

turtle_shapes = ["Classic", "Turtle", "Arrow", "Circle", "Square", "Triangle"]
shape_var = tk.StringVar(root)
shape_var.set(turtle_shapes[0])

for key in ["w", "W", "Up"]:
    root.bind(f"<{key}>", move_forward)

for key in ["s", "S", "Down"]:
    root.bind(f"<{key}>", move_backward)

for key in ["a", "A", "Left"]:
    root.bind(f"<{key}>", turn_left)

for key in ["d", "D", "Right"]:
    root.bind(f"<{key}>", turn_right)

for key in ["e", "E"]:
    root.bind(f"<{key}>", toggle_pen)
    
for key in ["f", "F"]:
    root.bind(f"<{key}>", toggle_turtle)

root.bind("<Button-1>", remove_focus)

# Description text paragraph
text_box_description = tk.Text(root, font=("Arial", 9), width=66, height=6, wrap="word",
                               bg="#f0f0f0", fg="black", bd=0, highlightthickness=0, spacing2=10)
text_box_description.place(x=1100, y=40)
text_box_description.tag_configure("bold", font=("Arial", 9, "bold"))
text_box_description.insert("1.0", "Risovalka", "bold")
text_box_description.insert("2.0", " is an editor in which the user can draw on the canvas with a single tool, the turtle. ")
text_box_description.insert("end", "The user can make changes in the turtle settings, changing the turtle itself and its behavior.")
text_box_description.config(state="disabled")

# Project information paragraph
text_project_information_window = tk.Text(root, font=("Arial", 9), width=40, height=1, wrap="word",
                               bg="#f0f0f0", fg="black", bd=0, highlightthickness=0, spacing2=10)
text_project_information_window.place(x=1100, y=156)
text_project_information_window.insert("1.0", "Click on the “📜” button to view project information")
text_project_information_window.config(state="disabled")

btn_open_project_information_window = tk.Button(root, text="📜" , font=("Arial", 10, "bold"), command=open_project_information_window)
btn_open_project_information_window.place(x=1832, y=146)

# Help text paragraph
text_help_window = tk.Text(root, font=("Arial", 9), width=40, height=1, wrap="word",
                               bg="#f0f0f0", fg="black", bd=0, highlightthickness=0, spacing2=10)
text_help_window.place(x=1100, y=208)
text_help_window.insert("1.0", "Click on the “?” button to view the key controls.")
text_help_window.config(state="disabled")

btn_open_help_window = tk.Button(root, text=" ? ", font=("Arial", 10, "bold"), command=open_help_window)
btn_open_help_window.place(x=1832, y=198)


# Turtle settings
label_settings = tk.Label(root, text="Turtle settings:", font=("Arial", 15))
label_settings.place(x=1100, y=260)

# Option step
label_option_step = tk.Label(root, text="Step length:", font=("Arial", 12))
label_option_step.place(x=1100, y=330)

pen_option_step_entry = tk.Entry(root, font=("Arial", 12), width=5)
pen_option_step_entry.insert(0, "10")
pen_option_step_entry.place(x=1264, y=332)
pen_option_step_entry.bind("<KeyRelease>", change_pen_step)

# Option turn
label_option_turn = tk.Label(root, text="Rotation angle:", font=("Arial", 12))
label_option_turn.place(x=1100, y=404)

pen_option_turn_entry = tk.Entry(root, font=("Arial", 12), width=5)
pen_option_turn_entry.insert(0, "10")
pen_option_turn_entry.place(x=1300, y=406)
pen_option_turn_entry.bind("<KeyRelease>", change_pen_turn)

# Option size
label_option_size = tk.Label(root, text="Pen size:", font=("Arial", 12))
label_option_size.place(x=1100, y=474)

pen_option_size_entry = tk.Entry(root, font=("Arial", 12), width=5)
pen_option_size_entry.insert(0, "1")
pen_option_size_entry.place(x=1228, y=476)
pen_option_size_entry.bind("<KeyRelease>", change_pen_size)

# Option pen color
label_option_pen_color = tk.Label(root, text="Pen color:", font=("Arial", 12))
label_option_pen_color.place(x=1100, y=544)

label_option_pen_color_display = tk.Label(root, text="COLOR", font=("Arial", 13))
label_option_pen_color_display.place(x=1232, y=545)

btn_option_pen_color = tk.Button(root, text="Choose pen color", command=change_pen_color, width=18)
btn_option_pen_color.place(x=1650, y=535)

# Option turtle shape
label_option_shape = tk.Label(root, text="Turtle shape:", font=("Arial", 12))
label_option_shape.place(x=1100, y=614)

label_option_shape_display = tk.Label(root, text=turtle_shapes[0].lower(), font=("Arial", 13))
label_option_shape_display.place(x=1270, y=614)

shape_option_shape_menu = tk.OptionMenu(root, shape_var, *turtle_shapes, command=change_turtle_shape)
shape_option_shape_menu.config(width=8)
shape_option_shape_menu.place(x=1716, y=610)

# Option turtle color
label_option_turtle_color = tk.Label(root, text="Turtle color:", font=("Arial", 12))
label_option_turtle_color.place(x=1100, y=684)

label_option_turtle_color_display = tk.Label(root, text="COLOR", font=("Arial", 13))
label_option_turtle_color_display.place(x=1254, y=685)

btn_option_turtle_color = tk.Button(root, text="Choose turtle color", command=change_turtle_color, width=18)
btn_option_turtle_color.place(x=1650, y=685)


# Other actions
label_actions = tk.Label(root, text="Key actions:", font=("Arial", 15))
label_actions.place(x=1100, y=750)

# Turtle position and teleportation
label_turtle_position = tk.Label(root, text="Position:", font=("Arial", 12))
label_turtle_position.place(x=1100, y=820)

label_turtle_position_values = tk.Label(root, text="X: 0, Y: 0, Angle: 0°", font=("Arial", 13))
label_turtle_position_values.place(x=1214, y=820)

btn_option_pen_color = tk.Button(root, text="Change position", width=18,
                                 command=lambda: open_position_window(root, set_new_position, t.xcor(), t.ycor(), t.heading()))
btn_option_pen_color.place(x=1650, y=820)


# Action buttons
btn_up = tk.Button(root, text=" ↑ ", font=("Arial", 12), command=move_forward)
btn_up.place(x=1160, y=904)

btn_down = tk.Button(root, text=" ↓ ", font=("Arial", 12), command=move_backward)
btn_down.place(x=1160, y=986)

btn_left = tk.Button(root, text="←", font=("Arial", 12), command=turn_left)
btn_left.place(x=1100, y=944)

btn_right = tk.Button(root, text="→", font=("Arial", 12), command=turn_right)
btn_right.place(x=1222, y=944)


btn_pen_updown = tk.Button(root, text="Pen up", command=toggle_pen, width=15)
btn_pen_updown.place(x=1310, y=904)

btn_turtle_visibility = tk.Button(root, text="Hide turtle", command=toggle_turtle, width=15)
btn_turtle_visibility.place(x=1310, y=990)

btn_clear_canvas = tk.Button(root, text="Clear Canvas", command=clear_canvas, width=12, bg="lightcoral")
btn_clear_canvas.place(x=1722, y=904)

btn_go_start = tk.Button(root, text="Print Canvas", command=lambda: save_canvas_screenshot(root, canvas, t), width=12, bg="lightblue")
btn_go_start.place(x=1722, y=990)


#canvas.focus_set()
root.mainloop()