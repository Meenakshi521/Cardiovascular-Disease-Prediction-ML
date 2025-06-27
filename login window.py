import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import csv

def fxn1():
    patient_id = patient.get()
    password = code.get()

    if patient_id == "admin" and password == "1234":
        window.destroy()  
    else:
        messagebox.showerror("Invalid", "Invalid username and password")

window = tk.Tk()
window.title("CARDIOVASCULAR DISEASE PREDICTION")
window.geometry("1700x900")
window.configure(bg="white")

# ICON IMAGE
path = "icon_image.png"
load = Image.open(path)
render = ImageTk.PhotoImage(load)
window.iconphoto(False, render)

# IMAGE
image = Image.open("image.png").resize((1550, 800))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image)
image_label.pack()
image_label.place(x=0, y=0)

# HEADING
heading = tk.Label(window, text="CARDIOVASCULAR DISEASE PREDICTION", bg="white", fg="black", font=("Algerian", 35))
heading.pack()

# FRAME
frame = tk.Frame(window, width=350, height=350, bg="white")
frame.place(x=1150, y=250)

heading = tk.Label(frame, text="Sign in", fg="black", bg="white", font=("Microsoft yaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

def on_enter(e):
    patient.delete(0, 'end')

def on_leave(e):
    name = patient.get()
    if name == '':
        patient.insert(0, "Patient_id")

patient = tk.Entry(frame, width=25, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
patient.place(x=30, y=80)
patient.insert(0, "Patient_id")
patient.bind('<FocusIn>', on_enter)
patient.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, "Password")

code = tk.Entry(frame, width=25, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# BUTTONS
tk.Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=fxn1).place(x=35, y=204)
label = tk.Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)
sign_up = tk.Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8")
sign_up.place(x=215, y=270)

window.mainloop()
