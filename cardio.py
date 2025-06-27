import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import csv
import pickle as pk
import pandas as pd

cardio_model=pk.load(open('cardiovascular_Model-2.pkl','rb'))
gc_encoder=pk.load(open('glucose and  cholesterol encoder-2.pkl','rb'))

cardio_data=pd.read_csv(r"C:\Users\hp\Downloads\Cardiovascular_Disease.csv")

window = tk.Tk()
window.title("CARDIOVASCULAR DISEASE PREDICTION")
window.geometry("1700x900")
window.configure(bg="white")

# ICON IMAGE
path = ("icon_image.png")
load = Image.open(path)
render = ImageTk.PhotoImage(load)
window.iconphoto(False, render)

def save_inputs():
    patient_name = Patient_name.get()
    age = Age.get()
    gender = gender_var.get()
    smoke = smoke_var.get()
    physical_activity = physical_activity_var.get()
    alcohol_intake = alcohol_intake_var.get()

    with open('patient_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([patient_name, age, gender, smoke, physical_activity, alcohol_intake])
    
    messagebox.showinfo("Saved", "Patient data has been saved successfully!")

def predict():
    patient_name = Patient_name.get()
    age = Age.get()
    gender = gender_var.get()
    smoke = smoke_var.get()
    physical_activity = physical_activity_var.get()
    alcohol_intake = alcohol_intake_var.get()

    # Dummy prediction logic (replace with real model prediction)
    if int(age) > 50 and smoke == "yes":
        prediction = "High risk of cardiovascular disease"
    else:
        prediction = "Low risk of cardiovascular disease"

    messagebox.showinfo("Prediction Result", f"Patient: {patient_name}\nPrediction: {prediction}")

def fxn1():
    patient_id = patient.get()
    password = code.get()

    if patient_id == "admin" and password == "1234":
        window2 = tk.Toplevel(window)
        window2.title("CARDIOVASCULAR DISEASE PREDICTION")
        window2.geometry("1800x950")

        # ICON
        path = ("icon_image.png")
        load = Image.open(path)
        render = ImageTk.PhotoImage(load)
        window2.iconphoto(False, render)

        # IMAGE
        image = Image.open("w2.png").resize((1700, 820))
        image = ImageTk.PhotoImage(image)
        image_label = tk.Label(window2, image=image)
        image_label.pack()
        image_label.place(x=-100, y=-245)

        # FRAME
        heading_entry = tk.Frame(window2, width=1650, height=400, bg="#2ad2db")
        heading_entry.place(x=0, y=500)

        # ENTRY
        tk.Label(heading_entry, text="Patient_name :-", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=230, y=20)
        global Patient_name
        Patient_name = tk.StringVar()
        Patient_name_entry = tk.Entry(window2, textvariable=Patient_name, width=15, font=("Bahnschrift Light", 25), bg="#2ad2db", fg="black", bd=10)
        Patient_name_entry.place(x=400, y=500)
        tk.Label(heading_entry, text="Age :-", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=900, y=20)
        global Age
        Age = tk.StringVar()
        Age_entry = tk.Entry(window2, textvariable=Age, width=15, font=("Bahnschrift Light", 25), bg="#2ad2db", fg="black", bd=10)
        Age_entry.place(x=980, y=500)

        # RADIO BUTTON1
        tk.Label(heading_entry, text="Gender", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=270, y=105)
        global gender_var
        gender_var = tk.StringVar(value="Male")
        radio_male = tk.Radiobutton(window2, text="Male", variable=gender_var, value="Male")
        radio_female = tk.Radiobutton(window2, text="Female", variable=gender_var, value="Female")
        radio_male.place(x=250, y=640)
        radio_female.place(x=300, y=640)

        # RADIO BUTTON2
        tk.Label(heading_entry, text="Smoke", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=585, y=105)
        global smoke_var
        smoke_var = tk.StringVar(value="no")
        radio_yes_smoke = tk.Radiobutton(window2, text="yes", variable=smoke_var, value="yes")
        radio_no_smoke = tk.Radiobutton(window2, text="no", variable=smoke_var, value="no")
        radio_yes_smoke.place(x=580, y=640)
        radio_no_smoke.place(x=620, y=640)

        # RADIO BUTTON3
        tk.Label(heading_entry, text="Physical_activity", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=850, y=105)
        global physical_activity_var
        physical_activity_var = tk.StringVar(value="yes")
        radio_yes_pa = tk.Radiobutton(window2, text="yes", variable=physical_activity_var, value="yes")
        radio_no_pa = tk.Radiobutton(window2, text="no", variable=physical_activity_var, value="no")
        radio_yes_pa.place(x=880, y=640)
        radio_no_pa.place(x=920, y=640)

        # RADIO BUTTON4
        tk.Label(heading_entry, text="Alcohol_intake", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=1180, y=105)
        global alcohol_intake_var
        alcohol_intake_var = tk.StringVar(value="no")
        radio_yes_alcohol = tk.Radiobutton(window2, text="yes", variable=alcohol_intake_var, value="yes")
        radio_no_alcohol = tk.Radiobutton(window2, text="no", variable=alcohol_intake_var, value="no")
        radio_yes_alcohol.place(x=1200, y=640)
        radio_no_alcohol.place(x=1240, y=640)

        # PREDICTION BUTTON
        tk.Button(window2, width=39, pady=7, text="PREDICT", bg="#28a4c9", fg="white", border=10, command=predict).place(x=650, y=700)

        # SAVE BUTTON
        tk.Button(window2, width=39, pady=7, text="SAVE", bg="#28a4c9", fg="white", border=10, command=save_inputs).place(x=1050, y=700)

        # LOGOUT 
        new_win = tk.Button(window2, text="LOGOUT", font=("Cooper", 12, "bold"), fg="black", bg="#2ad2db", border=10, width=10, relief="groove", command=window2.destroy)
        new_win.place(x=1400, y=30)

        window2.mainloop()
    else:
        messagebox.showerror("Invalid", "Invalid username and/or password")

# IMAGE
image = Image.open("image.png").resize((1550, 800))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image)
image_label.pack()
image_label.place(x=0, y=0)

# HEADING
heading = tk.Label(window, text="CARDIOVASCULAR_DISEASE_PREDICTION", bg="white", fg="black", font=("Brush Script MT", 35))
heading.place(x=350, y=0)
heading.pack()

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

# ENTRY
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